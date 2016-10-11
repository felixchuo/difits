# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_exe_progress_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='exercise_progress',
            field=models.CharField(default=b'NA', max_length=2, choices=[(b'NA', b'NOT ATTEMPTED'), (b'NC', b'NOT COMPLETED'), (b'CM', b'COMPLETED')]),
        ),
    ]
