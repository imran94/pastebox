# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 21:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pastebox', '0007_analytics'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytics',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 21, 52, 20, 320247, tzinfo=utc)),
        ),
    ]
