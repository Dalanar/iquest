# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_branches(apps, schema_editor):
    Branch = apps.get_model("main", "Branch")
    branch1 = Branch(address="Елизаровых, 56", phone="54-06-04")
    branch1.save()
    branch2 = Branch(address="Алтайская 8/3", phone="94-29-10")
    branch2.save()
    Quest = apps.get_model("main", "Quest")
    for quest in Quest.objects.all():
        if quest.id in [1, 2]:
            quest.branch = branch2
        else:
            quest.branch = branch1
        quest.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20160105_1736'),
    ]

    operations = [
        migrations.RunPython(add_branches),
    ]
