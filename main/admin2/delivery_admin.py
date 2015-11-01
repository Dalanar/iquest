__author__ = 'fs'

from django.contrib import admin
from django.conf.urls import patterns, url
import logging
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from main.models import QuestOrder

logger = logging.getLogger(__name__)


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



def send_emails(title, text):
    """
    ???????? ?????
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