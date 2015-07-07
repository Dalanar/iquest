from django.contrib import admin
from django.conf.urls import patterns, url
from django.shortcuts import render
from main.models import *
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage, EmailMultiAlternatives
from main.admin2.admin_models import PhoneImporter
from main.utils import *
import logging

logger = logging.getLogger(__name__)

class QuestOrderAdmin(admin.ModelAdmin):
    list_display = ('quest', 'time', 'date')
    date_hierarchy = 'date'


admin.site.register(GiftCardOrder)
admin.site.register(QuestOrder, QuestOrderAdmin)
admin.site.register(Quest)
admin.site.register(Ban)
admin.site.register(Phone)
admin.site.register(SmsDelivery)


class SettingAdmin(admin.ModelAdmin):
    readonly_fields = ('key',)


admin.site.register(Setting)

class PhoneImporterAdmin(admin.ModelAdmin):
    importer_template = 'admin/tools/phone-importer.html'

    def get_urls(self):
        urls = super(PhoneImporterAdmin, self).get_urls()
        my_urls = patterns('',
                           url(r'^$', self.admin_site.admin_view(self.import_phones),
                               name='phone-importer'),
        )
        return my_urls + urls

    def import_phones(self, request):
        success = False
        if request.method == 'POST':
            error = None
            try:
                numbers = request.POST['numbers']
                numbers = numbers.split()
                self.__add_numbers(numbers)
                success = True
            except Exception as e:
                error = str(e)
                logger.error("Exception when import contact: " + error)
            return render(
                request,
                self.importer_template,
                {
                    "success": success,
                    "error": error
                }
            )
        return render(
            request,
            self.importer_template
        )

    def __add_numbers(self, numbers):
        for number in numbers:
            number = phone_validate(number)
            if number:
                try:
                    Phone.objects.get(number=number)
                except Phone.DoesNotExist:
                    phone = Phone(number=number)
                    phone.save()


admin.site.register(PhoneImporter, PhoneImporterAdmin)


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


#admin.site.register(Delivery, DeliveryAdmin)


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
        emails = ("xcorter@mail.ru", "perseidsstarfall@gmail.com",)
        EmailMultiAlternatives()
        text_content = \
            get_template('admin/tools/email_template.plain').render(Context(ctx))
        html_content = \
            get_template('admin/tools/email_template.html').render(Context(ctx))
        msg = EmailMultiAlternatives(
            title,
            text_content,
            "noreply@iquest.tomsk.ru",
            emails
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        i+=1