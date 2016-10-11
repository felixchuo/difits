# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_auto_20160105_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='m_progress_details',
            name='progress',
        ),
        migrations.DeleteModel(
            name='M_Progress_Details',
        ),
    ]
