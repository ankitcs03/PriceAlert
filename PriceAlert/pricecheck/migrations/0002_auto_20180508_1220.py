# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-05-08 06:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricecheck', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='product_id',
            new_name='source',
        ),
    ]
