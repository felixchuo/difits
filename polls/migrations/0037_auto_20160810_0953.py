# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0036_auto_20160810_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutname',
            new_name='tutName',
        ),
    ]
