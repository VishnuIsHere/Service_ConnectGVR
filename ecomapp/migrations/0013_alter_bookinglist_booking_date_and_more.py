# Generated by Django 5.1.5 on 2025-01-22 08:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0012_alter_bookinglist_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinglist',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookinglist',
            name='register',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookinglist',
            name='service_request',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.servicerequest'),
            preserve_default=False,
        ),
    ]
