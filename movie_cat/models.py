from django.db import models
from django.db.models import Q
from movies.models import Video


class VideoCategory(models.Model):
	name = models.CharField(max_length=100,verbose_name="Название")
	slug = models.CharField(max_length=100,verbose_name="Англ. название для ссылки")
	order = models.PositiveSmallIntegerField(default=0,verbose_name="Порядковый номер")
	def __str__(self):
		return self.name
	class Meta:
		ordering = ["order","name"]
		verbose_name = "категория видео"
		verbose_name_plural = "категории видео"

	def __str__(self):
		return self.name

	def is_movies_exists(self):
		return Video.objects.filter(category_id=self.pk).exists()

	def get_movies(self):
		query = Q(category_id=self.pk)
		list = Video.objects.filter(query)
		return list

	def get_movies_10(self):
		query = Q(category_id=self.pk)
		list = Video.objects.filter(query)[:10]
		return list
