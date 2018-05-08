# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-05-07 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=250)),
                ('product_name', models.CharField(max_length=250)),
                ('alert_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('email_id', models.EmailField(max_length=70)),
            ],
        ),
    ]
