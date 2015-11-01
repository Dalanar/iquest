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
        if request.user.is_superuser:
            return qs
        return qs.filter(id=1)



class SettingAdmin(admin.ModelAdmin):
    readonly_fields = ('key',)


class SmsDeliveryAdmin(admin.ModelAdmin):
    readonly_fields = ('is_completed',)



admin.site.register(GiftCardOrder)
admin.site.register(QuestOrder, QuestOrderAdmin)
admin.site.register(Quest)
admin.site.register(Ban)
admin.site.register(Phone)
admin.site.register(SmsDelivery, SmsDeliveryAdmin)
admin.site.register(Setting)
admin.site.register(PhoneImporter, PhoneImporterAdmin)
#admin.site.register(Delivery, DeliveryAdmin)
