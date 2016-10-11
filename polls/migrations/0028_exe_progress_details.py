# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20160107_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exe_Progress_Details',
            fields=[
                ('exeProDetails', models.AutoField(serialize=False, primary_key=True)),
                ('exercise', models.IntegerField(blank=True)),
                ('exeQueNumStatus', models.IntegerField()),
                ('progress', models.ForeignKey(to='polls.Progress')),
            ],
        ),
    ]
