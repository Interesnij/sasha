# Generated by Django 2.2.15 on 2020-08-31 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_video_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='slug',
        ),
    ]
