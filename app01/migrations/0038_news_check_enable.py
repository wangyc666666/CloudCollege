# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0037_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='check_enable',
            field=models.BooleanField(default=False, verbose_name='是否审核'),
        ),
    ]
