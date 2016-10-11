# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_exercise_exequenum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mastery',
            old_name='mastery_question',
            new_name='masQueExpression',
        ),
        migrations.AddField(
            model_name='mastery',
            name='masQueLevel',
            field=models.CharField(default=0, max_length=1, choices=[(b'1', b'Simple'), (b'2', b'Moderate'), (b'3', b'Challenging')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mastery',
            name='masQueText',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mastery',
            name='masTotalWorkSteps',
            field=models.CharField(default=None, max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9')]),
            preserve_default=False,
        ),
    ]
