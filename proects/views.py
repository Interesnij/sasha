from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from django.views.generic import ListView
from proects.models import Proect


class ProectsListView(ListView, CategoryListMixin):
	model = Proect
    template_name="proects_index.html"

	def get_queryset(self):
		proects = Proect.objects.only("pk")
		return proects

class ProectView(TemplateView):
    template_name = "proect.html"

    def get(self,request,*args,**kwargs):
        self.proect = Proect.objects.get(slug=self.kwargs["slug"])
        return super(ProectView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(ProectView,self).get_context_data(**kwargs)
        context["object"] = self.proect
        return context
