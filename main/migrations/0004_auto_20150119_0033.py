# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20141211_2125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='giftcardorder',
            options={'verbose_name': 'Подарочная карта', 'verbose_name_plural': 'Подарочные карты'},
        ),
        migrations.AlterModelOptions(
            name='quest',
            options={'verbose_name': 'Квест', 'verbose_name_plural': 'Квесты'},
        ),
        migrations.AlterModelOptions(
            name='questorder',
            options={'verbose_name': 'Забронированый квест', 'verbose_name_plural': 'Забронированные квесты'},
        ),
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name': 'Время', 'verbose_name_plural': 'Время'},
        ),
        migrations.AlterField(
            model_name='giftcardorder',
            name='name',
            field=models.CharField(verbose_name='Имя', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='giftcardorder',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quest',
            name='quest',
            field=models.CharField(verbose_name='Квест', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questorder',
            name='date',
            field=models.DateField(verbose_name='Дата'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questorder',
            name='name',
            field=models.CharField(verbose_name='Имя', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questorder',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questorder',
            name='quest',
            field=models.ForeignKey(to='main.Quest', verbose_name='Квест'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questorder',
            name='time',
            field=models.ForeignKey(to='main.Time', verbose_name='Время'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='time',
            name='time',
            field=models.CharField(verbose_name='Время', max_length=50),
            preserve_default=True,
        ),
    ]
