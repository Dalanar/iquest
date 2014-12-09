from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from main.forms import GiftCardOrderForm, QuestOrderForm


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'


class ContactView(generic.TemplateView):
    template_name = 'main/contact.html'


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