from generic.mixins import CategoryListMixin
from django.views.generic import ListView
from forms.models import Blank


class FormsView(ListView, CategoryListMixin):
	model = Blank
	template_name="forms.html"

	def get_queryset(self):
		blanks = Blank.objects.only("pk")
		return blanks
