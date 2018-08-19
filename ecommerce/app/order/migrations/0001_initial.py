# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-15 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=250, null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('phone_number', models.CharField(max_length=250, null=True)),
                ('shipping_address', models.CharField(max_length=250, null=True)),
                ('tracking_number', models.CharField(max_length=250, null=True)),
                ('received_date', models.DateTimeField(auto_now_add=True)),
                ('total_charge', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
