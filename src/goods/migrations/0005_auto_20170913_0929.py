# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 01:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20170730_2112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分类1', 'verbose_name_plural': '分类2'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '订单', 'verbose_name_plural': '订单'},
        ),
    ]
