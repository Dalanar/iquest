# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20160214_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Имя изображения', max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='quests/gallery', blank=True, null=True)),
                ('preview', models.ImageField(upload_to='quests/gallery', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='quest',
            name='gallery',
            field=models.ManyToManyField(to='main.Image'),
            preserve_default=True,
        ),
    ]
