# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_auto_20161010_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cell_phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='work_phone',
            field=models.CharField(max_length=200),
        ),
    ]
