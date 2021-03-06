# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-21 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstack', '0037_customer_openstack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='backend_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='tenant',
            unique_together=set([('service_project_link', 'backend_id')]),
        ),
    ]
