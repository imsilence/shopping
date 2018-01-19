# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import goods.storage


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterField(
            model_name='category',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='img',
            field=models.ImageField(storage=goods.storage.FileStorage(), upload_to='goods/'),
        ),
        migrations.AlterField(
            model_name='goodsext',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
