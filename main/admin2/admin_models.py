__author__ = 'Stepan'

from django.db import models

class PhoneImporter(models.Model):
    class Meta(object):
        verbose_name = 'Импортировать телефоны'
        verbose_name_plural = "Импортировать телефоны"