# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150819_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_progress_details',
            name='mastery_score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='m_progress_details',
            name='question_progress',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='progress',
            name='skill',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_pmr',
            field=models.IntegerField(default=0),
        ),
    ]
