# Generated by Django 2.2.12 on 2023-02-11 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0003_auto_20230209_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
