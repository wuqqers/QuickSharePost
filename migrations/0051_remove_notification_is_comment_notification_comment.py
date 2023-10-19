# Generated by Django 4.2.6 on 2023-10-18 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialm', '0050_alter_comment_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_comment',
        ),
        migrations.AddField(
            model_name='notification',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='socialm.comment'),
        ),
    ]
