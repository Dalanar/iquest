# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('quest', models.CharField(choices=[(1, 'Случайный пациент'), (2, 'Время «Z»')], max_length=2)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[(1, '12:00-13:00'), (2, '13:00-14:00'), (3, '14:00-15:00'), (4, '15:00-16:00'), (5, '16:00-17:00'), (6, '17:00-18:00')], max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='giftcardorder',
            name='name',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
