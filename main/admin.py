from django.contrib import admin
from main.models import *
from main.admin2.admin_models import PhoneImporter, PhoneImporterAdmin
import logging

logger = logging.getLogger(__name__)


class QuestOrderAdmin(admin.ModelAdmin):
    list_display = ('quest', 'time', 'date')
    date_hierarchy = 'date'
    readonly_fields = ('notified',)

    def get_queryset(self, request):
        qs = super(QuestOrderAdmin, self).get_queryset(request)
        # TODO переписать на установку в админке
        if request.user.username == "iquestA":
            return qs.filter(quest__alias="enemy")
        if request.user.is_superuser:
            return qs
        return qs.filter(id=1)



class SettingAdmin(admin.ModelAdmin):
    readonly_fields = ('key',)


class SmsDeliveryAdmin(admin.ModelAdmin):
    readonly_fields = ('is_completed',)


class GiftCardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'activated',)
    list_filter = ('activated',)
    search_fields = ['card_number']
    readonly_fields = ('activated',)

    def save_model(self, request, card, form, change):
        if card.activated_in:
            card.activated = True
        else:
            card.activated = False
        card.save()


admin.site.register(GiftCardOrder)
admin.site.register(QuestOrder, QuestOrderAdmin)
admin.site.register(Quest)
admin.site.register(Branch)
admin.site.register(GiftCard, GiftCardAdmin)
admin.site.register(Ban)
admin.site.register(Phone)
admin.site.register(SmsDelivery, SmsDeliveryAdmin)
admin.site.register(Setting)
admin.site.register(PhoneImporter, PhoneImporterAdmin)
#admin.site.register(Delivery, DeliveryAdmin)
