# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-31 06:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '导航栏', 'verbose_name_plural': '导航栏'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
    ]