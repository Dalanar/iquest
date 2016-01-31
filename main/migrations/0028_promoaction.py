# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20160127_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoAction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание акции')),
                ('is_active', models.BooleanField(default=True, verbose_name='Акция активна')),
                ('image', models.ImageField(upload_to='promo/%Y/%m/%d')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
            bases=(models.Model,),
        ),
    ]
