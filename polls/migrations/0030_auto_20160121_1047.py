# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0029_progress_exercise_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='exe_progress_details',
            name='student',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='m_progress_details',
            name='student',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='t_progress_details',
            name='student',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
