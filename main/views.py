from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.utils import timezone
from main.forms import GiftCardOrderForm, QuestOrderForm
from main.models import Time, QuestOrder, Quest
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


def questsOrder(request):
    if request.method == "POST":
        try:
            time = int(request.POST['time'])
            time_obj = Time.objects.filter(pk=time)
            if not time_obj:
                return JsonResponse("Wrong request", status=400)
            date = request.POST['date']
            timestamp = int(ftime.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()))
            if timestamp < int(ftime.time()):
                return JsonResponse("Wrong time", status=400)
            quest = int(request.POST['quest'])
            quest = Quest.objects.filter(pk=quest)
            if not quest:
                return JsonResponse("Wrong request", status=400)
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            if name.strip() == "" or phone.strip() or email.strip() == "":
                return JsonResponse("Wrong request", status=400)
            quest_order = QuestOrder(quest=quest, name=name, phone=phone, email=email, time=time, date=date)
            quest_order.save()
        except:
            return JsonResponse("Something error", status=400)
    else:
        orders = QuestOrder.objects.filter(date__gte=timezone.now())
        orderJson = serializers.serialize("json", orders)
        return render(
            request,
            'main/quests.html',
            {
                "orderJson" : orderJson,
                "times": Time.objects.all()
            }
        )