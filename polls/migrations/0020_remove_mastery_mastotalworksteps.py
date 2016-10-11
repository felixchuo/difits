# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20160105_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mastery',
            name='masTotalWorkSteps',
        ),
    ]
