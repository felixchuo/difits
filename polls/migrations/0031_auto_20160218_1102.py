# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0030_auto_20160121_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exe_possible',
            name='exeFeedbackVisualAid',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='exe_working',
            name='exeHintVisualAid',
            field=models.CharField(max_length=255),
        ),
    ]
