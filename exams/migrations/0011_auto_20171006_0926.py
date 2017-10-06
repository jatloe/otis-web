# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0010_auto_20170818_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(blank=True, help_text='When the assignment should be due. Leave blank if not active this semester.', null=True),
        ),
    ]
