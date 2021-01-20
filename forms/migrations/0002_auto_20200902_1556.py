# Generated by Django 2.2.15 on 2020-09-02 15:56

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='blank',
            name='forms_blank_created_e3f9a3_brin',
        ),
        migrations.AddIndex(
            model_name='blank',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='Шаблоны зая_created_280433_brin'),
        ),
        migrations.AlterModelTable(
            name='blank',
            table='"Шаблоны заявлений"',
        ),
    ]
