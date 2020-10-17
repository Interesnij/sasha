from django.views.generic.base import ContextMixin
from django.conf import settings
from movie_cat.models import VideoCategory
from blog_cat.models import BlogCategory


class CategoryListMixin(ContextMixin):

	def get_context_data(self,**kwargs):
		context = super(CategoryListMixin,self).get_context_data(**kwargs)
		context["current_url"] = self.request.path
		context["movie_categories"] = VideoCategory.objects.only("pk")
		context["blog_categories"] = BlogCategory.objects.only("pk")
		return context
