# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0051_remove_news_videos_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='videos_url',
            field=models.CharField(max_length=300, null=True, blank=True, verbose_name='课程列表'),
        ),
    ]
