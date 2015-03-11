from django.contrib import admin
from django.conf.urls import patterns, url
from django.shortcuts import render
from main.models import *
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage
import logging

logger = logging.getLogger(__name__)

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


class DeliveryAdmin(admin.ModelAdmin):
    delivery_template = 'admin/tools/delivery.html'

    def get_urls(self):
        urls = super(DeliveryAdmin, self).get_urls()
        my_urls = patterns('',
                           url(r'^$', self.admin_site.admin_view(self.delivery_page),
                               name='admin-delivery'),
        )
        return my_urls + urls

    def delivery_page(self, request):
        if request.method == 'POST':
            error = None
            success = False
            try:
                title = request.POST['mail-title']
                text = request.POST['text']
                send_emails(title, text)
                success = True
            except Exception as e:
                logger.error("Exception when send email: " + str(e))
                error = str(e)
            return render(
                request,
                self.delivery_template,
                {
                    "success": success,
                    "error": error
                }
            )
        return render(
            request,
            self.delivery_template
        )


admin.site.register(Delivery, DeliveryAdmin)


def send_emails(title, text):
    """
    Рассылка писем
    """
    i = 0
    amount = 100
    while True:
        emails = QuestOrder.objects.all().order_by('id').values_list('email', flat=True).distinct()[i*amount:amount]
        if emails.count() == 0:
            break
        ctx = {
            "title": title,
            "text": text
        }
        a = ""
        for email in emails:
            a += email + ", "
        logger.error(a)
        message = get_template('admin/tools/email_template.html').render(Context(ctx))
        emails = ("xcorter@mail.ru", "perseidsstarfall@gmail.com",)
        msg = EmailMessage(title, message, to=emails, from_email="noreply@iquest.tomsk.ru")
        msg.content_subtype = 'html'
        msg.send()
        i+=1