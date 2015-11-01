# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def set_address(apps, schema_editor):
    Quest = apps.get_model("main", "Quest")
    for quest in Quest.objects.all():
        quest.address = 'Алтайская 8/3'
        quest.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150706_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneImporter',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Импортировать телефоны',
                'verbose_name': 'Импортировать телефоны',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='smsdelivery',
            options={'verbose_name_plural': 'Смс рассылка', 'verbose_name': 'Смс рассылка'},
        ),
        migrations.AddField(
            model_name='quest',
            name='address',
            field=models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quest',
            name='alias',
            field=models.CharField(max_length=255, blank=True, null=True, verbose_name='Псевдоним для обращения'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questorder',
            name='ip',
            field=models.CharField(max_length=11, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questorder',
            name='notified',
            field=models.BooleanField(default=False, verbose_name='Смс уведомление отправлено'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smsdelivery',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Завершена'),
            preserve_default=True,
        ),
        migrations.RunPython(set_address),
    ]
