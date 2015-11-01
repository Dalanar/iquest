__author__ = 'Stepan'

from django.db import models
from django.contrib import admin
from django.conf.urls import patterns, url
import logging
from django.shortcuts import render
from main.utils import *
from main.models import Phone

logger = logging.getLogger(__name__)


class PhoneImporter(models.Model):
    class Meta(object):
        verbose_name = 'Импортировать телефоны'
        verbose_name_plural = "Импортировать телефоны"


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