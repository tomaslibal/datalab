# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-12 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=128)),
                ('weight', models.FloatField(default=1.0)),
            ],
        ),
        migrations.AddField(
            model_name='datapoint',
            name='entity_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lab.Entity'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='description',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
