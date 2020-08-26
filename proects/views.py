from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class ProectsView(TemplateView, CategoryListMixin):
    template_name = "proects.html"
