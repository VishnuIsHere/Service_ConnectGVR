# Generated by Django 5.1.5 on 2025-01-21 03:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_rename_created_at_bookinglist_booking_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='register',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
