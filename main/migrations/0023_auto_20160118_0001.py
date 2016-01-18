# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def fill_quest_names(apps, schema_editor):
    Quest = apps.get_model("main", "Quest")
    for quest in Quest.objects.all():
        if not quest.alias:
            if quest.quest == "Время Z":
                quest.alias = "zombie"
            if quest.quest == "Враг народа":
                quest.alias = "enemy"
            if quest.quest == "hospital":
                quest.alias = "hospital"
            quest.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_giftcard_activated_time'),
    ]

    operations = [
        migrations.RunPython(fill_quest_names),
    ]
