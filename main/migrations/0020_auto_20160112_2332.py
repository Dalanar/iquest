# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20160112_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcard',
            name='status',
            field=models.CharField(choices=[('1', 'В печати'), ('2', 'В точке продажи'), ('3', 'Продана'), ('4', 'Активирована')], default=1, max_length=1),
            preserve_default=True,
        ),
    ]
