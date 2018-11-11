# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0080_auto_20180622_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentdata',
            name='newpic',
            field=models.ImageField(default='upload_imgss/logo.jpg', verbose_name='封面图片(160x120)', upload_to='upload_imgss'),
        ),
    ]
