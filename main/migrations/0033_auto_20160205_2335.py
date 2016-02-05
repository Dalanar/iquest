# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_quest_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promoaction',
            name='description',
        ),
        migrations.AddField(
            model_name='promoaction',
            name='full_image',
            field=models.ImageField(null=True, verbose_name='Полное изображение', upload_to='promo/%Y/%m/%d'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='promoaction',
            name='run_date',
            field=models.DateTimeField(null=True, verbose_name='Дата запуска', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='promoaction',
            name='image',
            field=models.ImageField(width_field=400, verbose_name='Превью 400 на 600', height_field=600, upload_to='promo/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
