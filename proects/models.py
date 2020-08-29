from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.postgres.indexes import BrinIndex
from pilkit.processors import ResizeToFill, ResizeToFit
from imagekit.models import ProcessedImageField


class Proect(models.Model):
	title = models.CharField(max_length=200, verbose_name="Название")
	slug = models.CharField(max_length=200, unique=True, verbose_name="Английский аналог для вставки в ссылку")
	description = RichTextUploadingField(config_name='default', external_plugin_resources=[('youtube','/static/ckeditor_plugins/youtube/youtube/','plugin.js',)],)
	created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
	image = ProcessedImageField(format='JPEG', options={'quality': 90}, upload_to="proects/proects", processors=[ResizeToFit(width=1024, upscale=False)])

	class Meta:
		ordering = ["-created"]
		verbose_name = "Проект"
		verbose_name_plural = "Проекты"
		indexes = (BrinIndex(fields=['created']),)

	def __str__(self):
		return self.title

	@classmethod
	def get_next_proect(cls, self):
		return cls.objects.filter(pk__gt=self.pk).order_by('pk').first()
