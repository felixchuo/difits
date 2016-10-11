# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20151210_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='exe_working',
            name='exeHintVisualAid',
            field=models.ImageField(default=0, upload_to=b''),
            preserve_default=False,
        ),
    ]
