# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_schedule(apps, schema_editor):
    Quest = apps.get_model("main", "Quest")
    Schedule = apps.get_model("main", "Schedule")
    Schedule.objects.all().delete()

    quests = Quest.objects.all()
    for quest in quests:
        schedule = Schedule()
        if quest.id == 1:
            schedule.weekday = '''10:30=1500
12:30=1500
14:30=2000
16:30=2000
18:30=2500
20:30=2500
22:30=2500'''
            schedule.weekday_before_weekend = schedule.weekday
            schedule.weekend = '''10:30=2000
12:30=2000
14:30=2500
16:30=2500
18:30=2500
20:30=2500
22:30=2500'''
            schedule.weekend_before_weekday = schedule.weekend
        elif quest.id == 2:
            schedule.weekday = '''10:00=2000
12:00=2000
14:00=2000
16:00=2500
18:00=3000
20:00=3000
22:00=3000'''
            schedule.weekday_before_weekend = schedule.weekday
            schedule.weekend = '''10:00=2500
12:00=2500
14:00=3000
16:00=3000
18:00=3000
20:00=3000
22:00=3000'''
            schedule.weekend_before_weekday = schedule.weekend
        elif quest.id == 3:
            schedule.weekday = '''14:30=1500
16:00=2000
17:30=2000
19:00=2000
20:30=2000
22:00=2000'''
            schedule.weekday_before_weekend = schedule.weekday
            schedule.weekend = '''11:00=2500
12:30=2500
14:00=2500
15:30=2500
17:00=2500
18:30=2500
20:00=2500
21:30=2500
23:00=2500'''
            schedule.weekend_before_weekday = schedule.weekend
        elif quest.id == 4:
            # outframe
            schedule.weekday = '''15:00=2000
16:30=2000
18:00=2500
19:30=2500
21:00=2500
22:30=2500'''
            schedule.weekday_before_weekend = schedule.weekday
            schedule.weekend = '''11:30=2500
13:00=2500
14:30=2500
16:00=2500
17:30=2500
19:00=2500
20:30=2500
22:00=2500
23:30=2500'''
            schedule.weekend_before_weekday = schedule.weekend
        elif quest.id == 5:
            #genius
            schedule.weekday = '''10:00=1500
11:30=1500
13:00=2000
14:30=2000
16:00=2000
17:30=2500
19:00=2500
20:30=2500
22:00=2500'''
            schedule.weekday_before_weekend = schedule.weekday
            schedule.weekend = '''10:00=2000
11:30=2000
13:00=2000
14:30=2500
16:00=2500
17:30=2500
19:00=2500
20:30=2500
22:00=2500'''
            schedule.weekend_before_weekday = schedule.weekend
        elif quest.id == 6:
            #hostel
            schedule.weekday = '''10:00=2000
11:30=2000
13:00=2500
14:30=2500
16:00=2500
17:30=3000
19:00=3000
20:30=3000
22:00=3000
23:30=3000'''
            schedule.weekday_before_weekend = schedule.weekday
            schedule.weekend = '''10:00=2500
11:30=2500
13:00=2500
14:30=3000
16:00=3000
17:30=3000
19:00=3000
20:30=3000
22:00=3000
23:30=3000'''
            schedule.weekend_before_weekday = schedule.weekend
        schedule.quest = quest
        schedule.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20160219_2350'),
    ]

    operations = [
        migrations.RunPython(add_schedule)
    ]
