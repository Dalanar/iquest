# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_ban'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('key', models.CharField(max_length=255, verbose_name='Ключ')),
                ('value', models.TextField(verbose_name='Значение')),
            ],
            options={
                'verbose_name_plural': 'Настройки',
                'verbose_name': 'Настройки',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='ban',
            options={'verbose_name_plural': 'Баны', 'verbose_name': 'Бан'},
        ),
    ]
