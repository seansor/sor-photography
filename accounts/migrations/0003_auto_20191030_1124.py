# Generated by Django 2.2.6 on 2019-10-30 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userbillinginfo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbillinginfo',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
