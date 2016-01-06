# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_quest_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('address', models.CharField(verbose_name='Адрес', null=True, max_length=255, blank=True)),
                ('phone', models.CharField(verbose_name='Телефон', null=True, max_length=255, blank=True)),
                ('prefix', models.CharField(verbose_name='Префикс', null=True, max_length=5, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('card_number', models.CharField(verbose_name='Номер карты', max_length=255)),
                ('selling_time', models.DateField(verbose_name='Дата продажи')),
                ('activated', models.BooleanField(verbose_name='Карта активирована', default=False)),
                ('activated_in', models.ForeignKey(verbose_name='Филиал', null=True, blank=True, to='main.Branch')),
            ],
            options={
                'verbose_name': 'Подарочная карта',
                'verbose_name_plural': 'Подарочные карты',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='giftcardorder',
            options={'verbose_name': 'Заявка на подарочную карту', 'verbose_name_plural': 'Заявки на подарочные карты'},
        ),
        migrations.RemoveField(
            model_name='quest',
            name='address',
        ),
        migrations.RemoveField(
            model_name='quest',
            name='phone',
        ),
        migrations.AddField(
            model_name='quest',
            name='branch',
            field=models.ForeignKey(verbose_name='Филиал', null=True, blank=True, to='main.Branch'),
            preserve_default=True,
        ),
    ]
