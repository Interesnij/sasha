from django.views.generic.base import ContextMixin
from django.conf import settings
from movie_cat.models import MovieCategory


class CategoryListMixin(ContextMixin):

	def get_context_data(self,**kwargs):
		context = super(CategoryListMixin,self).get_context_data(**kwargs)
		context["current_url"] = self.request.path
		context["movie_categories"] = MovieCategory.objects.only("pk")
		return context
