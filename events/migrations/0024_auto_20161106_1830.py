# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_event_extra_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='confirmation_mail_body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='confirmation_mail_subject',
            field=models.CharField(blank=True, max_length=78),
        ),
        migrations.AddField(
            model_name='event',
            name='rejection_mail_body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='rejection_mail_subject',
            field=models.CharField(blank=True, max_length=78),
        ),
    ]