# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20151214_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='exeQueNum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
