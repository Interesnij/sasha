# Generated by Django 2.2.15 on 2020-09-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200831_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='email address'),
            preserve_default=False,
        ),
    ]