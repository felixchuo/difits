# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20160105_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mas_Working',
            fields=[
                ('masWorkingStep', models.AutoField(serialize=False, primary_key=True)),
                ('masWorkStepAnswer', models.CharField(max_length=255)),
                ('masStepNo', models.CharField(max_length=10)),
                ('masRightFeedback', models.CharField(max_length=255)),
                ('masWrongFeedback', models.CharField(max_length=255)),
                ('masSuggestHint', models.CharField(max_length=255)),
                ('mastery', models.ForeignKey(to='polls.Mastery')),
            ],
        ),
    ]
