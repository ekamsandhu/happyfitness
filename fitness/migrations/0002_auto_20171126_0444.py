# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(max_length=1),
        ),
    ]
