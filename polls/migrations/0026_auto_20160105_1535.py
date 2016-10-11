# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20160105_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mas_working',
            name='masSuggestHint',
        ),
        migrations.AddField(
            model_name='mastery',
            name='masHint',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
