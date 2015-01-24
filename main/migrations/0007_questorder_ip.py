# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='questorder',
            name='ip',
            field=models.CharField(max_length=11, null=True),
            preserve_default=True,
        ),
    ]
