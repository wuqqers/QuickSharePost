# Generated by Django 4.2.6 on 2023-10-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialm', '0046_remove_likepost_created_on_remove_likepost_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='post_id',
            field=models.CharField(default='1', max_length=500),
        ),
    ]
