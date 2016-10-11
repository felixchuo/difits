# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_t_progress_details_animation_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_loginid',
            field=models.IntegerField(default=0),
        ),
    ]
