from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.utils import timezone
from main.forms import GiftCardOrderForm, QuestOrderForm
from main.models import QuestOrder, Quest, Ban, Setting, Phone
from main.schedule.api import get_schedule
import datetime, time as ftime, re
from main.smsc import SMSC
from main.utils import *
from main.modules.detectmobilebrowser import detect_mobile, is_mobile


def get_keywords():
    try:
        return Setting.objects.get(key="keywords").value
    except:
        return ""


class BaseMixin(object):

    def get_template_names(self):
        if detect_mobile(self.request):
            return self.template_name.replace('main', 'mobile')
        return self.template_name


    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        context["keywords"] = get_keywords()
        context["isMobile"] = is_mobile(self.request)
        return context


class IndexView(BaseMixin, generic.TemplateView):
    template_name = 'main/index.html'


class ContactView(BaseMixin, generic.TemplateView):
    template_name = 'main/contact.html'


class StubView(BaseMixin, generic.TemplateView):
    template_name = 'main/stub.html'


class RulesView(BaseMixin, generic.TemplateView):
    template_name = 'main/rules.html'


class FranchiseView(BaseMixin, generic.TemplateView):
    template_name = 'main/franchise.html'


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class CardsView(BaseMixin, AjaxableResponseMixin, CreateView):
    form_class = GiftCardOrderForm
    success_url = "/"
    template_name = 'main/cards.html'


class QuestsView(BaseMixin, AjaxableResponseMixin, CreateView):
    form_class = QuestOrderForm
    success_url = "/"
    template_name = 'main/quests.html'


# class AdminDeliveryView(generic.TemplateView):
#     template_name = 'admin/tools/delivery.html'


def error_json_response(message):
    return JsonResponse({"success": False, "message": message}, status=400)


def json_response(message):
    return JsonResponse({"success": True, "message": message}, status=200)


def check_time_in_schedule(date, time, cost, quest):
    schedule = get_schedule()
    order_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    for schedule_date in schedule:
        if schedule_date[0] == order_date.year and \
                        schedule_date[1] == order_date.month and \
                        schedule_date[2] == order_date.day:
            for key in schedule_date[4][quest]:
                if schedule_date[4][quest][key]["time"] == time and \
                                schedule_date[4][quest][key]["cost"] == cost:
                    return True
    return False


def quests_order(request):
    if request.method == "POST":
        try:
            try:
                ip = get_client_ip(request)
            except Exception:
                ip = ""
            bans = Ban.objects.all()
            for ban in bans:
                if ban.ip == ip:
                    return error_json_response("Banned")
            time = request.POST['time']
            cost = int(request.POST['cost'])
            date = request.POST['date']
            quest_id = int(request.POST['quest'])
            quest = Quest.objects.get(pk=quest_id)
            if not quest:
                return error_json_response("Wrong request")
            quest_id = quest_id - 1
            if not check_time_in_schedule(date, time, cost, quest_id):
                return error_json_response("Error data")
            timestamp = int(ftime.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()))
            current_time = int(ftime.time()) - 86400
            if timestamp < current_time:
                return error_json_response("Wrong time")
            name = request.POST['name'].strip()
            phone = request.POST['phone']
            phone = phone_validate(phone)
            email = request.POST.get('email')
            if email:
                email = request.POST['email'].strip()
                email = email.lower()
            else:
                email = ""
            if not data_validate(name, phone):
                return error_json_response("Wrong request")
            try:
                QuestOrder.objects.get(time=time, quest=quest, date=date)
            except QuestOrder.DoesNotExist:
                quest_order = QuestOrder(
                    quest=quest,
                    name=name,
                    phone=phone,
                    email=email,
                    time=time,
                    date=date,
                    cost=cost,
                    ip=ip
                )
                quest_order.save()
                send_sms(quest_order)
                add_phone_to_subscription(phone)
                return json_response("OK")
            else:
                return error_json_response("Quest already ordered")
        except Exception:
            return error_json_response("Something error")
    else:
        orders = QuestOrder.objects.filter(date__gte=timezone.now())
        orderJson = replace_orders(orders)
        quests = Quest.objects.all()
        questsIds = {
            "quest1": quests[0].id,
            "quest2": quests[1].id,
            "quest3": quests[2].id
        }
        template = 'main/quests.html'
        if detect_mobile(request):
            template = 'mobile/quests.html'
        return render(
            request,
            template,
            {
                "orderJson" : orderJson,
                "schedule": get_schedule(),
                "keywords": get_keywords(),
                'questsIds': questsIds
            }
        )


def replace_orders(orders):
    """
    QuestOrder[] orders
    """
    new_orders = []
    for order in orders:
        new_orders.append({
            'fields': {
                "quest": order.quest.id,
                "time": order.time,
                "date": order.date.isoformat(),
                "cost": order.cost
            }
        })
    return new_orders


def data_validate(name, phone):
    if name == "" or phone == "" or len(name) < 3:
        return False
    if not re.match(r"^[0-9\+\- ]+$", phone):
        return False
    return True


def get_client_ip(request):
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    http_x_real_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if http_x_real_ip:
        ip = http_x_real_ip
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_additional_sms_field():
    try:
        setting = Setting.objects.get(key="sms-additional")
    except Setting.DoesNotExist:
        return ""
    else:
        return setting.value


def add_phone_to_subscription(phone):
    try:
        phone = Phone.objects.get(number=phone)
    except Phone.DoesNotExist:
        phone = Phone(number=phone)
        phone.save()


def send_sms(quest_order):
    try:
        smsc = SMSC()
        template = 'Вы забронировали игру в IQuest :) "' + \
                   quest_order.quest.quest + '" ' + \
                   quest_order.date + ' ' +\
                   quest_order.time + ' ' + \
                   quest_order.quest.branch.address + '. ' + \
                   get_additional_sms_field()
        smsc.send_sms(quest_order.phone, template, sender="iquest")
    except Exception:
        return