from django.db import models

# Пустая модель для отчетов в админке
class Report(models.Model):
    class Meta(object):
        managed = False
        verbose_name = 'Отчет'
        verbose_name_plural = "Отчеты"