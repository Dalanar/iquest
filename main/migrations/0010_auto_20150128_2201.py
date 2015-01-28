# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def create_setting(apps, schema_editor):
    Setting = apps.get_model("main", "Setting")
    setting = Setting()
    setting.key = "keywords"
    setting.value = "квесты в реальности, томск, клаустрофобия, квест, куда пойти на новый год, куда сходить вечером, куда сходить сегодня, настольные игры, настольные игры томск, подарочные карты, чем заняться в томске, реалити квест, квесты в реальности, квесты в реальности томск, клаустрофобия, клаустрофобия квест, клаустрофобия томск, куда пойти на новый год, куда сходить вечером, куда сходить сегодня, настольные игры, настольные игры томск, подарочные карты, чем заняться в томске"
    setting.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150128_2200'),
    ]

    operations = [
        migrations.RunPython(create_setting),
    ]
