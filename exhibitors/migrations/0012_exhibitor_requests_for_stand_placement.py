# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0011_exhibitor_allergies'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='requests_for_stand_placement',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]