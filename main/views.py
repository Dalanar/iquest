from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView, SingleObjectMixin
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.utils import timezone
from main.forms import GiftCardOrderForm, QuestOrderForm
from main.models import QuestOrder, Quest, Setting, Phone, PromoAction, Branch
from main.schedule.api import get_schedule, check_time_in_schedule
import datetime, time as ftime, re
from main.smsc import SMSC
from main.utils import *
from main.modules.detectmobilebrowser import detect_mobile, is_mobile
import random
import logging
import iquest.settings as settings
from django.db.models import Q
from django.http import Http404
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


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

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        quests = Quest.objects.filter(is_active=True)
        context["quests"] = sorted(quests, key=lambda x: random.random())
        quests = Quest.objects.filter(is_active=False)
        quests = sorted(quests, key=lambda x: random.random())
        context["quests"] = context["quests"] + quests
        context["today"] = datetime.datetime.now()
        return context


class BaseTemplateView(BaseMixin, generic.TemplateView):
    template_name = ''


class ContactView(BaseMixin, generic.TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        branches = Branch.objects.all()
        context["branches"] = []
        for branch in branches:
            if branch.id == 2:
                context['main_branch'] = branch
            else:
                context["branches"].append(branch)
        return context


class PromoView(BaseMixin, generic.TemplateView):
    template_name = 'main/promo.html'

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        promos = PromoAction.objects.filter(
            Q(is_active=True),
            Q(run_date__lt=datetime.datetime.now()) | Q(run_date=None)
        )
        context["promos"] = promos
        return context


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


class QuestView(BaseMixin, AjaxableResponseMixin, CreateView, DetailView):
    form_class = QuestOrderForm
    success_url = "/"
    model = Quest
    template_name = 'blocks/quests/quest.html'
    slug_field = 'alias'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect(reverse('main:quests'))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(QuestView, self).get_context_data(**kwargs)
        context['today'] = datetime.datetime.now()
        orders = QuestOrder.objects.filter(date__gte=timezone.now())
        order_json = replace_orders(orders)
        context['orderJson'] = order_json
        context['schedule'] = get_schedule([self.object])
        context['keywords'] = get_keywords()
        context['form'] = QuestOrderForm()
        return context


def error_json_response(message):
    return JsonResponse({"success": False, "message": message}, status=400)


def json_response(message):
    return JsonResponse({"success": True, "message": message}, status=200)


def quests_order(request):
    quests = Quest.objects.filter(is_active=True)
    if request.method == "POST":
        try:
            time = request.POST['time']
            cost = int(request.POST['cost'])
            date = request.POST['date']
            quest_id = int(request.POST['quest'])
            quest = Quest.objects.get(pk=quest_id)
            if not quest:
                return error_json_response("Wrong request")
            if not check_time_in_schedule(date, time, cost, quest_id, quests):
                return error_json_response("Error data")
            timestamp = int(ftime.mktime(
                datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()
            ))
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
                    ip=""
                )
                quest_order.save()
                send_sms(quest_order)
                add_phone_to_subscription(phone)
                if datetime.datetime.strptime(date, "%Y-%m-%d").date() == datetime.date.today():
                    notify_operator(quest_order)
                return json_response("OK")
            else:
                return error_json_response("Quest already ordered")
        except Exception as e:
            logger.error("Exception: " + str(e))
            return error_json_response("Something error")
    else:
        orders = QuestOrder.objects.filter(date__gte=timezone.now())
        order_json = replace_orders(orders)
        template = 'main/quests.html'
        if detect_mobile(request):
            template = 'mobile/quests.html'
        return render(
            request,
            template,
            {
                "orderJson": order_json,
                "schedule": get_schedule(quests),
                "keywords": get_keywords(),
                'form': QuestOrderForm(),
                'quests': quests
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
        if not settings.debug:
            smsc.send_sms(quest_order.phone, template, sender="iquest")
    except Exception:
        return


def notify_operator(quest_order):
    try:
        smsc = SMSC()
        message = ', '.join([quest_order.quest.short_name,
                            str(quest_order.time),
                            quest_order.phone])
        if not settings.debug:
            smsc.send_sms(quest_order.quest.branch.operator_phone, message, sender="iquest")
    except Exception as ex:
        return