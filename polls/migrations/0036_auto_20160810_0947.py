# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0035_tutorial_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='name',
            new_name='tutname',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutLevel',
            field=models.CharField(default=1, max_length=1, choices=[(b'1', b'Simple'), (b'2', b'Moderate'), (b'3', b'Challenging')]),
            preserve_default=False,
        ),
    ]
