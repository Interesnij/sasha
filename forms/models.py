from django.db import models
from django.contrib.postgres.indexes import BrinIndex


class BlankCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name="Название")
	slug = models.CharField(max_length=100, verbose_name="Англ. название для ссылки")
	order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")
	def __str__(self):
		return self.name
	class Meta:
		ordering = ["order", "name"]
		verbose_name = "категория блога"
		verbose_name_plural = "категории блога"

	def __str__(self):
		return self.name


class Blank(models.Model):
	title = models.CharField(max_length=200, verbose_name="Название")
	file = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name="Документ")
	created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
	order = models.PositiveIntegerField(default=0)
	category = models.ManyToManyField(BlankCategory, blank=True, null=True, verbose_name="Категория")

	class Meta:
		ordering = ["order"]
		verbose_name = "Документ"
		verbose_name_plural = "Документы"
		indexes = (BrinIndex(fields=['created']),)

	def get_blank(self):
		filename = self.file.name.split('/')[-1]
		return filename
