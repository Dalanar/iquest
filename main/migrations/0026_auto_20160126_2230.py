# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_new_project(apps, schema_editor):
    Branch = apps.get_model("main", "Branch")
    Quest = apps.get_model("main", "Quest")

    branch = Branch.objects.get(address="Елизаровых, 56")
    branch.save()
    quest = Quest(quest="out-frame", alias="hostel", branch=branch)
    quest.save()

    branch = Branch(address="Вершинина 38", phone="34-43-34", prefix="")
    branch.save()
    quest = Quest(quest="У.М.Н.И.К.", alias="genius", branch=branch)
    quest.save()

    branch = Branch(address="Нижне-Луговая 13/1", phone="32-08-36", prefix="")
    branch.save()
    quest = Quest(quest="Переполох в общаге", alias="hostel", branch=branch)
    quest.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20160119_2057'),
    ]

    operations = [
        migrations.RunPython(create_new_project),
    ]
