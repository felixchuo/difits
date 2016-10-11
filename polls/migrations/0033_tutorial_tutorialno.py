# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_auto_20160321_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tutorialNo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
