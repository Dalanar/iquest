from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.utils import timezone
from main.forms import GiftCardOrderForm, QuestOrderForm
from main.models import QuestOrder, Quest
from main.schedule import schedule
from django.core import serializers
import datetime, time as ftime


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'


class ContactView(generic.TemplateView):
    template_name = 'main/contact.html'


class StubView(generic.TemplateView):
    template_name = 'main/stub.html'


class RulesView(generic.TemplateView):
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


class CardsView(AjaxableResponseMixin, CreateView):
    form_class = GiftCardOrderForm
    success_url = "/"
    template_name = 'main/cards.html'


class QuestsView(AjaxableResponseMixin, CreateView):
    form_class = QuestOrderForm
    success_url = "/"
    template_name = 'main/quests.html'


def error_json_response(message):
    return JsonResponse({"success": False, "message": message}, status=400)


def json_response(message):
    return JsonResponse({"success": True, "message": message}, status=200)


def check_time_in_schedule(date, time, cost):
    weekday = int(datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%w'))
    for key in schedule[weekday]:
        if schedule[weekday][key]["time"] == time and schedule[weekday][key]["cost"] == cost:
            return True
    return False


def quests_order(request):
    if request.method == "POST":
        try:
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
            if name == "" or phone == "" or email == "":
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
                    cost=cost
                )
                quest_order.save()
                return json_response("OK")
            else:
                return error_json_response("Quest already ordered")
        except Exception:
            return error_json_response("Something error")
    else:
        orders = QuestOrder.objects.filter(date__gte=timezone.now())
        orderJson = serializers.serialize("json", orders)
        # scheduleJson = serializers.serialize("json", schedule)
        return render(
            request,
            'main/quests.html',
            {
                "orderJson" : orderJson,
                "schedule": schedule
            }
        )