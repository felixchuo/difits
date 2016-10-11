# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_exe_working_exehintvisualaid'),
    ]

    operations = [
        migrations.AddField(
            model_name='exe_possible',
            name='exeFeedbackVisualAid',
            field=models.ImageField(default=0, upload_to=b''),
            preserve_default=False,
        ),
    ]
