# Generated by Django 4.0.4 on 2022-12-19 04:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_facilities_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Facilities',
            new_name='Facility',
        ),
    ]