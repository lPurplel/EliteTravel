# Generated by Django 5.1.2 on 2024-10-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0013_alter_booking_flight_plane_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_flight',
            name='plane_image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
