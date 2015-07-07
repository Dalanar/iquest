# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150128_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
                'verbose_name': 'Рассылка',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='questorder',
            name='notified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
