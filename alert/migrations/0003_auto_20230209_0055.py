# Generated by Django 2.2.12 on 2023-02-09 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0002_alerts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alerts',
            new_name='Alert',
        ),
    ]