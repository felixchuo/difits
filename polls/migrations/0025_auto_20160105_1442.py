# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20160105_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Progress_Details',
            fields=[
                ('mpd', models.AutoField(serialize=False, primary_key=True)),
                ('mastery', models.IntegerField(blank=True)),
                ('question_progress', models.CharField(max_length=10)),
                ('mastery_score', models.IntegerField()),
                ('progress', models.ForeignKey(to='polls.Progress')),
            ],
        ),
        migrations.CreateModel(
            name='Mas_Working',
            fields=[
                ('masWorkingStep', models.AutoField(serialize=False, primary_key=True)),
                ('masWorkStepAnswer', models.CharField(max_length=255)),
                ('masStepNo', models.IntegerField()),
                ('masRightFeedback', models.CharField(max_length=255)),
                ('masWrongFeedback', models.CharField(max_length=255)),
                ('masSuggestHint', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mastery',
            fields=[
                ('mastery', models.AutoField(serialize=False, primary_key=True)),
                ('masQueText', models.CharField(max_length=255)),
                ('masQueExpression', models.CharField(max_length=255)),
                ('masQueLevel', models.CharField(max_length=1, choices=[(b'1', b'Simple'), (b'2', b'Moderate'), (b'3', b'Challenging')])),
                ('masTotalWorkSteps', models.CharField(max_length=255)),
                ('skill', models.ForeignKey(to='polls.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='mas_working',
            name='mastery',
            field=models.ForeignKey(to='polls.Mastery'),
        ),
    ]
