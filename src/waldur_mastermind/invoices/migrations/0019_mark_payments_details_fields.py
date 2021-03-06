# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 13:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0018_genericinvoiceitem_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='account',
            new_name='_account',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='address',
            new_name='_address',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='bank',
            new_name='_bank',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='company',
            new_name='_company',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='country',
            new_name='_country',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='email',
            new_name='_email',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='phone',
            new_name='_phone',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='postal',
            new_name='_postal',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='type',
            new_name='_type',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='accounting_start_date',
            new_name='_accounting_start_date',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='default_tax_percent',
            new_name='_default_tax_percent',
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_account',
            field=models.CharField(blank=True, editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_address',
            field=models.CharField(blank=True, editable=False, max_length=300),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_bank',
            field=models.CharField(blank=True, editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_company',
            field=models.CharField(blank=True, editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_country',
            field=models.CharField(blank=True, editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_email',
            field=models.EmailField(blank=True, editable=False, max_length=75),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_phone',
            field=models.CharField(blank=True, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_postal',
            field=models.CharField(blank=True, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_type',
            field=models.CharField(blank=True, editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_accounting_start_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False,
                                       verbose_name='Start date of accounting'),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='_default_tax_percent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=4,
                                      validators=[django.core.validators.MinValueValidator(0),
                                                  django.core.validators.MaxValueValidator(100)]),
        ),
    ]
