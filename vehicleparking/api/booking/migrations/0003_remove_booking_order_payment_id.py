# Generated by Django 3.0.8 on 2023-04-21 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20230421_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='order_payment_id',
        ),
    ]
