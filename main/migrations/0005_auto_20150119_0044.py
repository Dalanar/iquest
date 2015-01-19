# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150119_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='questorder',
            name='cost',
            field=models.IntegerField(null=True, verbose_name='Стоимость', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questorder',
            name='time',
            field=models.CharField(verbose_name='Время', max_length=10),
            preserve_default=True,
        ),
    ]
