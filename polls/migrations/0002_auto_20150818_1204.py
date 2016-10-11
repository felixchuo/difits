# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='student_id',
            new_name='student_id_id',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='student_id',
            new_name='student_id_id',
        ),
    ]
