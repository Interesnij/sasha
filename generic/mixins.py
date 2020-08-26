from django.views.generic.base import ContextMixin
from django.conf import settings
from category.models import Category
from diary.models import DiaryCategory
from taggit.models import Tag


class CategoryListMixin(ContextMixin):
	tags=Tag.objects.all()
	def get_context_data(self,**kwargs):
		context=super(CategoryListMixin,self).get_context_data(**kwargs)
		context["current_url"]=self.request.path
		context["categories"]=Category.objects.all()
		context["diary_categories"]=DiaryCategory.objects.all()
		context["tags"]=self.tags
		return context

class PageNumberMixin(CategoryListMixin):
	def get_context_data(self,**kwargs):
		context=super(PageNumberMixin,self).get_context_data(**kwargs)
		try:
			context["pn"]=self.request.GET["page"]
		except KeyError:
			context["pn"]="1"
		return context
