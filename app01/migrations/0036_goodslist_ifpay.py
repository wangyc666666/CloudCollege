# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0035_auto_20171120_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodslist',
            name='ifpay',
            field=models.BooleanField(default=False, verbose_name='是否付款'),
        ),
    ]