# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20160207_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='alias',
            field=models.SlugField(verbose_name='Псевдоним для обращения', max_length=255, blank=True, unique=True, null=True),
            preserve_default=True,
        ),
    ]
