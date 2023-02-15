# Generated by Django 4.1.6 on 2023-02-14 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0007_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='alert',
            name='latitude',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='alert',
            name='longitude',
            field=models.CharField(max_length=20),
        ),
    ]
