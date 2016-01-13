from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from main.models import *
from main.admin2.admin_models import PhoneImporter, PhoneImporterAdmin
from django.contrib.admin.models import LogEntry
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
    list_display = ('card_number', 'activated_in', 'status',)
    list_filter = ('status',('selling_time', DateRangeFilter), 'activated_in',)
    search_fields = ['card_number']
    readonly_fields = ('card_number',)

    def get_readonly_fields(self, request, card=None):
        if card and not card.activated_in: # editing an existing object
            return self.readonly_fields
        return self.readonly_fields + ('status',)

    def save_model(self, request, card, form, change):
        is_exist = bool(card.id)
        prefix = card.branch.prefix
        card.save()
        if is_exist:
            return
        id = str(card.id)
        if len(id) == 1:
            id = '000' + id
        elif len(id) == 2:
            id = '00' + id
        elif len(id) == 3:
            id = '0' + id
        if prefix:
            card.card_number = prefix + id
        else:
            card.card_number = id
        card.save()


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'action_time')

admin.site.register(GiftCardOrder)
admin.site.register(QuestOrder, QuestOrderAdmin)
admin.site.register(Quest)
admin.site.register(Branch)
admin.site.register(GiftCard, GiftCardAdmin)
admin.site.register(Ban)
admin.site.register(Phone)
admin.site.register(SmsDelivery, SmsDeliveryAdmin)
admin.site.register(Setting)
admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(PhoneImporter, PhoneImporterAdmin)
#admin.site.register(Delivery, DeliveryAdmin)
