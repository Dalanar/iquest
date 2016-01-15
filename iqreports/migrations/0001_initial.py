# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
            bases=(models.Model,),
        ),
    ]
