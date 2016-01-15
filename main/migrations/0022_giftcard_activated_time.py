# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20160112_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftcard',
            name='activated_time',
            field=models.DateField(blank=True, verbose_name='Дата активации', null=True),
            preserve_default=True,
        ),
    ]
