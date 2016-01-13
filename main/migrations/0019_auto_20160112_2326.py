# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20160112_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('card_number', models.CharField(verbose_name='Номер карты', max_length=255)),
                ('selling_time', models.DateField(verbose_name='Дата продажи')),
                ('status', models.CharField(choices=[('1', 'В печати'), ('2', 'В точке продажи'), ('3', 'Продана'), ('4', 'Активирована')], max_length=1)),
                ('activated_in', models.ForeignKey(blank=True, verbose_name='Активирована в', null=True, to='main.Branch', related_name='card_activated_in')),
                ('branch', models.ForeignKey(related_name='card_branch', verbose_name='Локация', to='main.Branch')),
            ],
            options={
                'verbose_name': 'Подарочная карта',
                'verbose_name_plural': 'Подарочные карты',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'Филиалы', 'verbose_name': 'Филиал'},
        ),
    ]
