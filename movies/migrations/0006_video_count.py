# Generated by Django 2.2.15 on 2020-08-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]
