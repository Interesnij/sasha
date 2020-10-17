from django.db import models
from django.db.models import Q
from blog.models import Blog


class BlogCategory(models.Model):
	name = models.CharField(max_length=100,verbose_name="Название")
	slug = models.CharField(max_length=100,verbose_name="Англ. название для ссылки")
	order = models.PositiveSmallIntegerField(default=0,verbose_name="Порядковый номер")
	def __str__(self):
		return self.name
	class Meta:
		ordering = ["order","name"]
		verbose_name = "категория блога"
		verbose_name_plural = "категории блога"

	def __str__(self):
		return self.name

	def is_movies_exists(self):
		return Blog.objects.filter(category_id=self.pk).exists()

	def get_articles_10(self):
		query = Q(category_id=self.pk)
		list = Blog.objects.filter(query)[:10]
		return list

	def get_articles(self):
		query = Q(category_id=self.pk)
		list = Blog.objects.filter(query)
		return list
