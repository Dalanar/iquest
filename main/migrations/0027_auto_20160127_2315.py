# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def change_name(apps, schema_editor):
    Quest = apps.get_model("main", "Quest")

    quest = Quest.objects.get(quest="out-frame")
    quest.quest = "За кадром"
    quest.alias = "out-frame"
    quest.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20160126_2230'),
    ]

    operations = [
        migrations.RunPython(change_name),
    ]
