from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField


class User(AbstractUser):
    last_activity = models.DateTimeField(default=timezone.now, blank=True, verbose_name='Активность')
    avatar = ProcessedImageField(format='JPEG', options={'quality': 90}, upload_to="users/%Y/%m/%d/", processors=[ResizeToFit(width=500, upscale=False)], verbose_name="Аватар")
    email = models.EmailField(null=True, blank=True, unique=True, verbose_name='Email')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
