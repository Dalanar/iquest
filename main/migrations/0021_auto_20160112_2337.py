# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20160112_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcard',
            name='card_number',
            field=models.CharField(blank=True, null=True, verbose_name='Номер карты', max_length=255),
            preserve_default=True,
        ),
    ]
