from django.conf.urls import patterns, url
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contact$', views.BaseTemplateView.as_view(template_name="main/contact.html"), name='contact'),
    url(r'^rules$', views.BaseTemplateView.as_view(template_name="main/rules.html"), name='rules'),
    url(r'^cards', views.CardsView.as_view(), name='cards'),
    url(r'^promo', views.PromoView.as_view(), name='promo'),
    url(r'^quests/(?P<slug>[a-zA-Z\-]+)', views.QuestView.as_view(), name='show_quest'),
    url(r'^quests', views.quests_order, name='quests'),
    url(r'^franchise', views.BaseTemplateView.as_view(template_name="main/franchise.html"), name='franchise'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)