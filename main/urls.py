from django.conf.urls import patterns, include, url
from main import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^rules$', views.RulesView.as_view(), name='rules'),
    url(r'^cards', views.CardsView.as_view(), name='cards'),
    url(r'^quests', views.QuestsView.as_view(), name='quests'),
)