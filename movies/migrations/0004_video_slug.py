# Generated by Django 2.2.15 on 2020-08-31 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200831_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.CharField(default='', max_length=100, verbose_name='Англ. название для ссылки'),
            preserve_default=False,
        ),
    ]
