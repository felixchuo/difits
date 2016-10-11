# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0031_auto_20160218_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='m_progress_details',
            name='mas_adv_progress',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='m_progress_details',
            name='mas_easy_progress',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='m_progress_details',
            name='mas_mod_progress',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
