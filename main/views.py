from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.utils import timezone
from main.forms import GiftCardOrderForm, QuestOrderForm
from main.models import QuestOrder, Quest, Ban, Setting
from main.schedule import schedule
from django.core import serializers
import datetime, time as ftime, re


def get_keywords():
    try:
        return Setting.objects.get(key="keywords").value
    except:
        return ""


class KeywordsMixin(object):
    def get_context_data(self, **kwargs):
        context = super(KeywordsMixin, self).get_context_data(**kwargs)
        context["keywords"] = get_keywords()
        return context


class IndexView(KeywordsMixin, generic.TemplateView):
    template_name = 'main/index.html'


class ContactView(KeywordsMixin, generic.TemplateView):
    template_name = 'main/contact.html'


class StubView(KeywordsMixin, generic.TemplateView):
    template_name = 'main/stub.html'


class RulesView(KeywordsMixin, generic.TemplateView):
    template_name = 'main/rules.html'


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


class CardsView(KeywordsMixin, AjaxableResponseMixin, CreateView):
    form_class = GiftCardOrderForm
    success_url = "/"
    template_name = 'main/cards.html'


class QuestsView(KeywordsMixin, AjaxableResponseMixin, CreateView):
    form_class = QuestOrderForm
    success_url = "/"
    template_name = 'main/quests.html'


# class AdminDeliveryView(generic.TemplateView):
#     template_name = 'admin/tools/delivery.html'


def error_json_response(message):
    return JsonResponse({"success": False, "message": message}, status=400)


def json_response(message):
    return JsonResponse({"success": True, "message": message}, status=200)


def check_time_in_schedule(date, time, cost):
    weekday = int(datetime.datetime.strptime(date, "%Y-%m-%d").weekday())
    for key in schedule[weekday]:
        if schedule[weekday][key]["time"] == time and schedule[weekday][key]["cost"] == cost:
            return True
    return False


def quests_order(request):
    if request.method == "POST":
        try:
            ip = get_client_ip(request)
            bans = Ban.objects.all()
            for ban in bans:
                if ban.ip == ip:
                    return error_json_response("Banned")
            time = request.POST['time']
            cost = int(request.POST['cost'])
            date = request.POST['date']
            if not check_time_in_schedule(date, time, cost):
                return error_json_response("Error data")
            timestamp = int(ftime.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()))
            current_time = int(ftime.time()) - 86400
            if timestamp < current_time:
                return error_json_response("Wrong time")
            quest = int(request.POST['quest'])
            quest = Quest.objects.get(pk=quest)
            if not quest:
                return error_json_response("Wrong request")
            name = request.POST['name'].strip()
            phone = request.POST['phone'].strip()
            email = request.POST['email'].strip()
            email = email.lower()
            if not data_validate(name, email, phone):
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
                return json_response("OK")
            else:
                return error_json_response("Quest already ordered")
        except Exception:
            return error_json_response("Something error")
    else:
        orders = QuestOrder.objects.filter(date__gte=timezone.now())
        orderJson = replace_orders(orders)
        return render(
            request,
            'main/quests.html',
            {
                "orderJson" : orderJson,
                "schedule": schedule,
                "keywords": get_keywords()
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


def data_validate(name, email, phone):
    if name == "" or phone == "" or email == "" or len(name) < 3:
        return False
    if not re.match(r"^[0-9\+\- ]+$", phone):
        return False
    return True


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip