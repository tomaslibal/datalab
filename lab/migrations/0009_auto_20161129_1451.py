# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-29 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_datapoint_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDefinedEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('entity_type', models.CharField(choices=[('img', 'Image Entity'), ('generic', 'Generic')], default='img', max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='entity_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lab.UserDefinedEntity'),
        ),
        migrations.DeleteModel(
            name='Entity',
        ),
    ]
