# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_exe_possible_exefeedbackvisualaid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exeTotalWorkSteps',
            field=models.CharField(max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9')]),
        ),
    ]
