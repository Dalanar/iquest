# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20160105_1802'),
    ]

    operations = [
        migrations.DeleteModel(name='GiftCard'),
    ]
