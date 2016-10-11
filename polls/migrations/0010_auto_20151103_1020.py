# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20151027_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ex_possible',
            old_name='exWorkingStep',
            new_name='exWorking',
        ),
        migrations.RenameField(
            model_name='ex_possible',
            old_name='ex_Possibl',
            new_name='ex_Possible',
        ),
        migrations.RenameField(
            model_name='ex_working',
            old_name='exSequenceNo',
            new_name='exWorkStepNo',
        ),
        migrations.RenameField(
            model_name='ex_working',
            old_name='exWorkingStep',
            new_name='exWorking',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exercise_NOWS',
            new_name='exNoWorkSteps',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exercise_question',
            new_name='exQueExpression',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exercise_q_level',
            new_name='exQueLevel',
        ),
        migrations.AddField(
            model_name='exercise',
            name='exQueText',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
