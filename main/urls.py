from django.conf.urls import patterns, include, url
from main import views
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^rules$', views.RulesView.as_view(), name='rules'),
    url(r'^cards', views.CardsView.as_view(), name='cards'),
    url(r'^quests/occasional-patient', TemplateView.as_view(template_name="main/quests/occasional-patient.html"), name='quest_occasional-patient'),
    url(r'^quests/time-z', TemplateView.as_view(template_name="main/quests/time-z.html"), name='quest_time-z'),
    url(r'^quests/enemy', TemplateView.as_view(template_name="main/quests/enemy.html"), name='quest_enemy'),
    url(r'^quests/genius', TemplateView.as_view(template_name="main/quests/genius.html"), name='quest_genius'),
    url(r'^quests/out-frame', TemplateView.as_view(template_name="main/quests/out-frame.html"), name='quest_out-frame'),
    url(r'^quests/hostel', TemplateView.as_view(template_name="main/quests/out-frame.html"), name='quest_hostel'),
    url(r'^quests', views.quests_order, name='quests'),
    url(r'^franchise', views.FranchiseView.as_view(), name='franchise'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)