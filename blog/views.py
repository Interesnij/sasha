from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class BlogView(TemplateView, CategoryListMixin):
    template_name = "blog.html"
