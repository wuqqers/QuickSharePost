# Generated by Django 4.2.6 on 2023-10-18 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('socialm', '0042_profile_last_notification_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='likepost',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
