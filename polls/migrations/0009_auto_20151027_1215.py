# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_student_student_loginid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ex_Possible',
            fields=[
                ('ex_Possibl', models.AutoField(serialize=False, primary_key=True)),
                ('exPossibleMistake', models.CharField(max_length=255)),
                ('exMistakeFeedback', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ex_Working',
            fields=[
                ('exWorkingStep', models.AutoField(serialize=False, primary_key=True)),
                ('exSequenceNo', models.IntegerField()),
                ('exStepAnswer', models.CharField(max_length=255)),
                ('exStepHint', models.CharField(max_length=255)),
                ('exGeneralFeedback', models.CharField(max_length=255)),
                ('exCongratulatory', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exercise', models.AutoField(serialize=False, primary_key=True)),
                ('exercise_question', models.CharField(max_length=255)),
                ('exercise_q_level', models.CharField(max_length=1, choices=[(b'1', b'Simple'), (b'2', b'Moderate'), (b'3', b'Challenging')])),
                ('exercise_NOWS', models.IntegerField()),
                ('skill', models.ForeignKey(to='polls.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='ex_working',
            name='exercise',
            field=models.ForeignKey(to='polls.Exercise'),
        ),
        migrations.AddField(
            model_name='ex_possible',
            name='exWorkingStep',
            field=models.ForeignKey(to='polls.Ex_Working'),
        ),
    ]
