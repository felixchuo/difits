# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_remove_mastery_mastotalworksteps'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastery',
            name='masTotalWorkSteps',
            field=models.IntegerField(default=1),
        ),
    ]
