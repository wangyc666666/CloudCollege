# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0044_documentdata_check_enable'),
    ]

    operations = [
        migrations.CreateModel(
            name='GotVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='购买时间')),
                ('myvideo', models.ManyToManyField(blank=True, null=True, to='app01.News')),
            ],
            options={
                'verbose_name_plural': '我购买等视频',
                'verbose_name': '我购买等视频',
            },
        ),
    ]