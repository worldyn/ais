# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_auto_20170306_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.Campaign'),
        ),
    ]
