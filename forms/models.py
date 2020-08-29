from django.db import models
from django.contrib.postgres.indexes import BrinIndex
from django.http import HttpResponse


class Blank(models.Model):
	title = models.CharField(max_length=200, verbose_name="Название")
	file = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name="Документ")
	created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")

	class Meta:
		ordering = ["-created"]
		verbose_name = "Документ"
		verbose_name_plural = "Документы"
		indexes = (BrinIndex(fields=['created']),)

	def get_blank(self):
		filename = self.file.name.split('/')[-1]
		response = HttpResponse(self.file, content_type='text/plain')
		response['Content-Disposition'] = 'attachment; filename=%s' % filename
		return response
