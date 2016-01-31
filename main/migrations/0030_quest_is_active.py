# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def change_name(apps, schema_editor):
    Quest = apps.get_model("main", "Quest")

    quests = Quest.objects.all()
    for quest in quests:
        if quest.alias != "out-frame" and quest.alias != "hostel":
            quest.is_active = True
            quest.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_quest_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='is_active',
            field=models.BooleanField(verbose_name='Квест запущен', default=False),
            preserve_default=True,
        ),
        migrations.RunPython(change_name),
    ]
