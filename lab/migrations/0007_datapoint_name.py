# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-18 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_auto_20161115_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
