# Generated by Django 2.2.6 on 2019-10-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0005_auto_20191018_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
