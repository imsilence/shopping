# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 03:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20170913_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activeuserreport',
            old_name='status_time',
            new_name='report_time',
        ),
        migrations.RenameField(
            model_name='salereport',
            old_name='status_time',
            new_name='report_time',
        ),
    ]
