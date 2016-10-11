# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_mastery_mastotalworksteps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastery',
            name='masTotalWorkSteps',
            field=models.CharField(max_length=255),
        ),
    ]
