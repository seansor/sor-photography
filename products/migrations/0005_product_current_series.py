# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-11 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_collection_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='current_series',
            field=models.BooleanField(default=False),
        ),
    ]
