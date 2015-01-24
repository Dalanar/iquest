# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_questorder_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('ip', models.CharField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
