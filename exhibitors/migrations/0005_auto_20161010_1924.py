# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0004_auto_20161006_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitor',
            name='invoice_address_zip_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
