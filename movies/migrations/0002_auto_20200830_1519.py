# Generated by Django 2.2.15 on 2020-08-30 15:20

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie_cat', '0002_auto_20200830_1519'),
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='videovotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='videocommentvotes',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.VideoComment'),
        ),
        migrations.AddField(
            model_name='videocommentvotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='videocomment',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Комментатор'),
        ),
        migrations.AddField(
            model_name='videocomment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_comment_replies', to='movies.VideoComment', verbose_name='Родительский комментарий'),
        ),
        migrations.AddField(
            model_name='videocomment',
            name='video_comment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='movies.Video'),
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_category', to='movie_cat.VideoCategory', verbose_name='Плейлист'),
        ),
        migrations.AddField(
            model_name='video',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AddIndex(
            model_name='videocomment',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='movies_vide_created_75eea9_brin'),
        ),
        migrations.AddIndex(
            model_name='video',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='movies_vide_created_a91117_brin'),
        ),
    ]
