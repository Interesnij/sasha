# Generated by Django 2.2.15 on 2020-08-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200830_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocomment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
