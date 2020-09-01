from django.db import models
from django.contrib.postgres.indexes import BrinIndex
from django.utils import timezone
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField
from django.db.models import Q


class Friend(models.Model):
    image = ProcessedImageField(format='JPEG',
                                options={'quality': 90},
                                upload_to="friends/%Y/%m/%d/",
                                processors=[ResizeToFit(width=500, upscale=False)],
                                verbose_name="Логотип")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    link = models.CharField(max_length=255, verbose_name="Ссылка на друга")

    class Meta:
        verbose_name = "Дружественный проект"
        verbose_name_plural = "Дружественный проекты"
        indexes = (BrinIndex(fields=['created']),)
        ordering = ["-pk"]

    def __str__(self):
        return self.link
