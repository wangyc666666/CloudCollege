# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0041_auto_20171128_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='发布时间'),
        ),
    ]
