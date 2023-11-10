# Generated by Django 4.1.3 on 2023-10-31 19:44


import django.core.validators
import django.db.models.deletion
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOffer',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                (
                    'max_price',
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=14,
                        validators=[django.core.validators.MinValueValidator(0.0)],
                        verbose_name='purchase price',
                    ),
                ),
                (
                    'car',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='customer_offers',
                        related_query_name='customer offers',
                        to='core.carmodel',
                        verbose_name='car specified in offer',
                    ),
                ),
                (
                    'customer',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='offers',
                        related_query_name='offers',
                        to='customer.customermodel',
                        verbose_name='offer of the customer',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Customer offer',
                'verbose_name_plural': 'Customers offer',
                'db_table': 'CustomerOffer',
            },
        ),
    ]