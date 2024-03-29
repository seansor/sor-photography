# Generated by Django 2.2.6 on 2019-10-24 11:20

from django.db import migrations, models
from datetime import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0006_quote_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='date',
            field=models.DateField(default=datetime.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='price_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
