# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20160105_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mas_working',
            name='mastery',
        ),
        migrations.RemoveField(
            model_name='mastery',
            name='skill',
        ),
        migrations.DeleteModel(
            name='Mas_Working',
        ),
        migrations.DeleteModel(
            name='Mastery',
        ),
    ]
