from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied


class User(AbstractUser):
    last_activity = models.DateTimeField(default=timezone.now, blank=True, verbose_name='Активность')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
