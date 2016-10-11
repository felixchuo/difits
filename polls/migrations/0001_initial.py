# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('progress_id', models.AutoField(serialize=False, primary_key=True)),
                ('skill_id', models.IntegerField(max_length=10)),
                ('tutorial_progress', models.CharField(max_length=2, choices=[(b'NA', b'NOT ATTEMPTED'), (b'NC', b'NOT COMPLETED'), (b'CM', b'COMPLETED')])),
                ('mastery_progress', models.CharField(max_length=2, choices=[(b'NA', b'NOT ATTEMPTED'), (b'NC', b'NOT COMPLETED'), (b'CM', b'COMPLETED')])),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_id', models.AutoField(serialize=False, primary_key=True)),
                ('skill_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(serialize=False, primary_key=True)),
                ('student_firstname', models.CharField(max_length=200)),
                ('student_lastname', models.CharField(max_length=200)),
                ('student_class', models.CharField(max_length=10)),
                ('student_school', models.CharField(max_length=1, choices=[(b'1', b'KOLEJ DPAH ABDILLAH'), (b'2', b'SMK BATU LINTANG'), (b'3', b'SMK KUCHING HIGH'), (b'4', b'SMK GREEN ROAD'), (b'5', b'SMK SG. MAONG')])),
                ('student_dob', models.DateTimeField(verbose_name=b'Date of Birth')),
                ('student_gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('student_pmr', models.IntegerField(default=0, max_length=1)),
                ('student_maths', models.CharField(max_length=1, choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E'), (b'F', b'F')])),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='student_id',
            field=models.ForeignKey(to='polls.Student'),
        ),
        migrations.AddField(
            model_name='progress',
            name='student_id',
            field=models.ForeignKey(to='polls.Student'),
        ),
    ]
