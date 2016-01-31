# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_promoaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='image',
            field=models.ImageField(upload_to='quests/main', blank=True, null=True),
            preserve_default=True,
        ),
    ]
