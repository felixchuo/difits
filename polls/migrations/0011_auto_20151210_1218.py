# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20151103_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exe_Possible',
            fields=[
                ('exe_Possible', models.AutoField(serialize=False, primary_key=True)),
                ('exePossibleMistake', models.CharField(max_length=255)),
                ('exeMistakeFeedback', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Exe_Working',
            fields=[
                ('exeWorkingStep', models.AutoField(serialize=False, primary_key=True)),
                ('exeWorkStepNo', models.IntegerField()),
                ('exeStepAnswer', models.CharField(max_length=255)),
                ('exeStepHint', models.CharField(max_length=255)),
                ('exeGeneralFeedback', models.CharField(max_length=255)),
                ('exeCongratulatory', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='ex_possible',
            name='exWorking',
        ),
        migrations.RemoveField(
            model_name='ex_working',
            name='exercise',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exQueExpression',
            new_name='exeQueExpression',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exQueLevel',
            new_name='exeQueLevel',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exQueText',
            new_name='exeQueText',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='exNoWorkSteps',
            new_name='exeTotalWorkSteps',
        ),
        migrations.DeleteModel(
            name='Ex_Possible',
        ),
        migrations.DeleteModel(
            name='Ex_Working',
        ),
        migrations.AddField(
            model_name='exe_working',
            name='exercise',
            field=models.ForeignKey(to='polls.Exercise'),
        ),
        migrations.AddField(
            model_name='exe_possible',
            name='exeWorkingStep',
            field=models.ForeignKey(to='polls.Exe_Working'),
        ),
    ]
