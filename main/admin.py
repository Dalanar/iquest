from django.contrib import admin
from main.models import *


class QuestOrderAdmin(admin.ModelAdmin):
    list_display = ('quest', 'time', 'date')
    date_hierarchy = 'date'

admin.site.register(GiftCardOrder)
admin.site.register(QuestOrder, QuestOrderAdmin)
admin.site.register(Quest)
admin.site.register(Ban)


class SettingAdmin(admin.ModelAdmin):
    readonly_fields = ('key',)

admin.site.register(Setting, SettingAdmin)
