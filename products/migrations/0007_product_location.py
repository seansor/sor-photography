# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-11 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20191011_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default='', max_length=254),
        ),
    ]