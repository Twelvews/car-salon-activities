# Generated by Django 4.1.3 on 2023-11-16 13:21


from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='transmission_type',
            field=models.CharField(
                choices=[('manual', 'Manual'), ('auto', 'Auto')],
                max_length=50,
                verbose_name='transmission type of the car',
            ),
        ),
    ]