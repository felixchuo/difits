# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150820_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_progress_details',
            name='animation_progress',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
