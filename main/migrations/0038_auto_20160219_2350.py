# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20160217_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestPromo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст акции', default='')),
                ('run_date', models.DateTimeField(null=True, verbose_name='Дата запуска', blank=True)),
                ('quest', models.OneToOneField(to='main.Quest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('weekday', models.TextField(verbose_name='Расписание на будние дни', default='')),
                ('weekday_before_weekend', models.TextField(verbose_name='Будний день перед выходным', default='')),
                ('weekend', models.TextField(verbose_name='Расписание на выходные', default='')),
                ('weekend_before_weekday', models.TextField(verbose_name='Выходной перед будним днем', default='')),
                ('quest', models.OneToOneField(to='main.Quest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='quest',
            name='image',
            field=models.ImageField(null=True, verbose_name='Галерея', blank=True, upload_to='quests/main'),
            preserve_default=True,
        ),
    ]
