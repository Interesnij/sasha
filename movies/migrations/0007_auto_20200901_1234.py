# Generated by Django 2.2.15 on 2020-09-01 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_video_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-created'], 'verbose_name': 'Видео-ролики', 'verbose_name_plural': 'Видео-ролики'},
        ),
    ]
