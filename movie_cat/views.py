from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from django.views.generic import ListView
from movie_cat.models import VideoCategory
from movies.models import Video


class MovieListView(ListView, CategoryListMixin):
	model = Video
	template_name = "movies_index.html"
	paginate_by = 20

	def get(self,request,*args,**kwargs):
		if self.kwargs["slug"] == None:
			self.cat = VideoCategory.objects.first()
		else:
			self.cat = VideoCategory.objects.get(slug=self.kwargs["slug"])
		return super(MovieListView,self).get(request,*args,**kwargs)

	def get_queryset(self):
		videos = Video.objects.filter(category=self.cat)
		return videos

	def get_context_data(self,**kwargs):
		context = super(MovieListView,self).get_context_data(**kwargs)
		context["category"] = self.cat
		return context

class AboutView(TemplateView, CategoryListMixin):
    template_name = "movies_list.html"
