# Generated by Django 2.2.6 on 2019-10-18 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commissionorder',
            old_name='client',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='commissionorder',
            name='quote',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commissions.Quote'),
        ),
    ]