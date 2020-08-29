from django.db import models


class MovieCategory(models.Model):
	name = models.CharField(max_length=100,verbose_name="Название")
	order = models.PositiveSmallIntegerField(default=0,verbose_name="Порядковый номер")
	def __str__(self):
		return self.name
	class Meta:
		ordering = ["order","name"]
		verbose_name = "категория видео"
		verbose_name_plural = "категории видео"

	def __str__(self):
		return self.name
