# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_mas_working'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mas_working',
            name='masStepNo',
            field=models.IntegerField(),
        ),
    ]
