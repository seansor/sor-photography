# Generated by Django 2.2.6 on 2019-10-17 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_works', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_travel', models.DecimalField(decimal_places=2, max_digits=6)),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CommissionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('size', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=254)),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quote', models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='commissions.Quote')),
            ],
        ),
    ]