# Generated by Django 5.1.2 on 2024-10-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_booking_flight_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_flight',
            name='booking_time',
            field=models.IntegerField(),
        ),
    ]
