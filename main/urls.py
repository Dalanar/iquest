from django.conf.urls import patterns, url
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^rules$', views.RulesView.as_view(), name='rules'),
    url(r'^cards', views.CardsView.as_view(), name='cards'),
    url(r'^promo', views.PromoView.as_view(), name='promo'),
    url(r'^quests/(?P<slug>[a-zA-Z\-]+)', views.QuestView.as_view(), name='show_quest'),
    url(r'^quests', views.quests_order, name='quests'),
    url(r'^franchise', views.FranchiseView.as_view(), name='franchise'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)