# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0033_tutorial_tutorialno'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='e_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='progress',
            name='m_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='progress',
            name='t_status',
            field=models.IntegerField(default=0),
        ),
    ]
