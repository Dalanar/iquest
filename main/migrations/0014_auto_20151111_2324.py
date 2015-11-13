# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_quest(apps, schema_editor):
    Quest = apps.get_model("main", "Quest")
    quest = Quest(quest="Враг народа", alias="enemy", address="Елизаровых, 56")
    quest.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20151101_1919'),
    ]

    operations = [
         migrations.RunPython(add_quest),
    ]
