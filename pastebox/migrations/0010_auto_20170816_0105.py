# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pastebox', '0009_auto_20170816_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
