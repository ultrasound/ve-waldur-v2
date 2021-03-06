# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0050_reset_cloud_spl_quota_limits'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='agreement_number',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=75, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='phone number'),
        ),
    ]
