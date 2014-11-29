from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'


class ContactView(generic.TemplateView):
    template_name = 'main/contact.html'


class RulesView(generic.TemplateView):
    template_name = 'main/rules.html'