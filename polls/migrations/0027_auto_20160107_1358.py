# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20160105_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mas_working',
            name='masRightFeedback',
        ),
        migrations.RemoveField(
            model_name='mas_working',
            name='masWrongFeedback',
        ),
        migrations.AddField(
            model_name='mastery',
            name='masRightFeedback',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mastery',
            name='masWrongFeedback',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
