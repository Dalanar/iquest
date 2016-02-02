from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from main.models import *
from main.admin2.admin_models import PhoneImporter, PhoneImporterAdmin
from django.contrib.admin.models import LogEntry
from django.db.models import Q
import datetime
import logging

logger = logging.getLogger(__name__)


class QuestOrderAdmin(admin.ModelAdmin):
    list_display = ('quest', 'time', 'date')
    date_hierarchy = 'date'
    readonly_fields = ('notified',)

    def get_queryset(self, request):
        qs = super(QuestOrderAdmin, self).get_queryset(request)
        profile = request.user.profile
        if request.user.is_superuser:
            return qs
        if request.user.profile:
            branches_ids = list(map(lambda branch: branch.id, profile.branch.all()))
            return qs.filter(quest__branch__id__in=branches_ids)
        return qs



class SettingAdmin(admin.ModelAdmin):
    readonly_fields = ('key',)


class SmsDeliveryAdmin(admin.ModelAdmin):
    readonly_fields = ('is_completed',)


class GiftCardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'branch', 'activated_in', 'status',
                    'activated_time',)
    list_filter = ('status',('selling_time', DateRangeFilter), 'activated_in',)
    search_fields = ['card_number']
    readonly_fields = ('card_number', 'activated_time',)

    def get_readonly_fields(self, request, card=None):
        if card and not card.activated_in: # editing an existing object
            return self.readonly_fields
        return self.readonly_fields + ('status',)

    def save_model(self, request, card, form, change):
        is_exist = bool(card.id)
        prefix = card.branch.prefix
        if card.activated_in:
            card.status = 4
        if not card.activated_time and card.status == 4:
            card.activated_time = datetime.datetime.now()
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
admin.site.register(Branch)
admin.site.register(GiftCard, GiftCardAdmin)
admin.site.register(Ban)
admin.site.register(Phone)
admin.site.register(SmsDelivery, SmsDeliveryAdmin)
admin.site.register(Setting)
admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(PhoneImporter, PhoneImporterAdmin)
#admin.site.register(Delivery, DeliveryAdmin)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'профиль'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class PromoActionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ['name']
    fields = ('name', 'description', 'image_tag', 'image', 'created_at',)
    readonly_fields = ('image_tag', 'created_at',)

admin.site.register(PromoAction, PromoActionAdmin)

class QuestAdmin(admin.ModelAdmin):
    fields = ('quest', 'description', 'alias', 'is_active', 'branch', 'image_tag', 'image',)
    list_display = ('id', 'quest',)
    readonly_fields = ('image_tag',)

admin.site.register(Quest, QuestAdmin)