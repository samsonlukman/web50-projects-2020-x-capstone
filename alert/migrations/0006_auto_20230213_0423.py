# Generated by Django 2.2.12 on 2023-02-13 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0005_auto_20230211_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='latitude',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='alert',
            name='longitude',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='alert',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
