# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150818_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Progress_Details',
            fields=[
                ('mpd', models.AutoField(serialize=False, primary_key=True)),
                ('question_progress', models.IntegerField(max_length=3)),
                ('mastery_score', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Mastery',
            fields=[
                ('mastery', models.AutoField(serialize=False, primary_key=True)),
                ('mastery_question', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='T_Progress_Details',
            fields=[
                ('tpd', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('tutorial', models.AutoField(serialize=False, primary_key=True)),
                ('tutorial_animation', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='progress_id',
            new_name='progress',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='skill_id',
            new_name='skill',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='skill_id',
            new_name='skill',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_id',
            new_name='student',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='skill',
            field=models.ForeignKey(to='polls.Skill'),
        ),
        migrations.AddField(
            model_name='t_progress_details',
            name='progress',
            field=models.ForeignKey(to='polls.Progress'),
        ),
        migrations.AddField(
            model_name='t_progress_details',
            name='tutorial',
            field=models.ForeignKey(to='polls.Tutorial'),
        ),
        migrations.AddField(
            model_name='mastery',
            name='skill',
            field=models.ForeignKey(to='polls.Skill'),
        ),
        migrations.AddField(
            model_name='m_progress_details',
            name='mastery',
            field=models.ForeignKey(to='polls.Mastery'),
        ),
        migrations.AddField(
            model_name='m_progress_details',
            name='progress',
            field=models.ForeignKey(to='polls.Progress'),
        ),
    ]
