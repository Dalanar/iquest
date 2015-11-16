# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_phones(apps, schema_editor):
    Quest = apps.get_model("main", "Quest")
    for quest in Quest.objects.all():
        if quest.address == 'Алтайская 8/3':
            quest.phone = "94-29-10"
        else:
            quest.phone = "54-06-04"
        quest.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20151111_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='phone',
            field=models.CharField(verbose_name='Телефон', null=True, blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.RunPython(add_phones),
    ]
