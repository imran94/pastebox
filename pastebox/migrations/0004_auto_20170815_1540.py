# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebox', '0003_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(blank=True, default=None, max_length=5, null=True, unique=True),
        ),
    ]
