# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-10 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='', max_length=254),
        ),
    ]