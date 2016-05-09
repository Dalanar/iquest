# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20160302_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='operator_phone',
            field=models.CharField(max_length=20, default='', verbose_name='Телефон оператора', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quest',
            name='short_name',
            field=models.CharField(max_length=5, default='', verbose_name='Сокращенное название'),
            preserve_default=False,
        ),
    ]
