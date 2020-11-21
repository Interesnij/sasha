from django.db import models
from django.db.models import Q



class Appeal(models.Model):
	name = models.CharField(max_length=100,verbose_name="Название")
	order = models.PositiveSmallIntegerField(default=0,verbose_name="Порядковый номер")
	description = models.CharField(max_length=1000, blank=True, verbose_name="Описание")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["order", "name"]
		verbose_name = "Призыв"
		verbose_name_plural = "Призывы"

	def __str__(self):
		return self.name

	def likes_count(self):
		likes = AppealVotes.objects.filter(parent=self, vote__gt=0).values("pk")
		count = likes.count()
		if count:
			return count
		else:
			return ''


class AppealVotes(models.Model):
    LIKE = 1
    DISLIKE = -1
    VOTES = ((DISLIKE, 'Не нравится'),(LIKE, 'Нравится'))

    vote = models.IntegerField(default=0, verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    parent = models.ForeignKey(Appeal, on_delete=models.CASCADE)
