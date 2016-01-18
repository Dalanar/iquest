from django.conf.urls import patterns, include, url
from main import views
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^rules$', views.RulesView.as_view(), name='rules'),
    url(r'^cards', views.CardsView.as_view(), name='cards'),
    url(r'^quests/occasional-patient', TemplateView.as_view(template_name="main/quests/occasional-patient.html"), name='quest_occasional-patient'),
    url(r'^quests/time-z', TemplateView.as_view(template_name="main/quests/time-z.html"), name='quest_time-z'),
    url(r'^quests/enemy', TemplateView.as_view(template_name="main/quests/enemy.html"), name='quest_enemy'),
    url(r'^quests', views.quests_order, name='quests'),
    url(r'^franchise', views.FranchiseView.as_view(), name='franchise'),
)