# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0005_auto_20161010_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cataloginfo',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='cataloginfo',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='cataloginfo',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='cataloginfo',
            name='website_url',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
