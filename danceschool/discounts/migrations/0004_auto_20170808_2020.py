# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-09 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0003_auto_20170724_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountcombo',
            name='daysInAdvanceRequired',
            field=models.PositiveIntegerField(blank=True, help_text='For this discount to apply, all components must be satisfied by events that begin this many days in the future (measured from midnight of the date of registration).  Leave blank for no restriction.', null=True, verbose_name='Must register __ days in advance'),
        ),
        migrations.AddField(
            model_name='discountcombo',
            name='expirationDate',
            field=models.DateTimeField(blank=True, help_text='Leave blank for no expiration.', null=True, verbose_name='Expiration Date'),
        ),
    ]
