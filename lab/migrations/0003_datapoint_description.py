# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-14 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20161112_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='description',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
