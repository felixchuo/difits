# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150819_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='student',
        ),
        migrations.AlterField(
            model_name='m_progress_details',
            name='mastery',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='t_progress_details',
            name='tutorial',
            field=models.IntegerField(verbose_name=polls.models.Tutorial),
        ),
    ]
