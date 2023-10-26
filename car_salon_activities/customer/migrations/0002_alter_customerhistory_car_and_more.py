# Generated by Django 4.1.3 on 2023-10-26 21:06


import django.db.models.deletion
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('jauth', '0003_user_is_verified'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerhistory',
            name='car',
            field=models.CharField(max_length=50, verbose_name='car'),
        ),
        migrations.AlterField(
            model_name='customerhistory',
            name='showroom',
            field=models.CharField(max_length=50, verbose_name='showroom'),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='user',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to='jauth.user',
                verbose_name='user instance',
            ),
        ),
    ]
