# Generated by Django 2.2.6 on 2019-10-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0002_auto_20191018_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='price_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
