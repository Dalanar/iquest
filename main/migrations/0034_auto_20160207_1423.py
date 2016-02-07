# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20160205_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promoaction',
            name='image',
            field=models.ImageField(upload_to='promo/%Y/%m/%d', verbose_name='Превью 400 на 600'),
            preserve_default=True,
        ),
    ]
