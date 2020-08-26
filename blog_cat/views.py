from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class BlogCatView(TemplateView, CategoryListMixin):
    template_name = "blog_cat.html"
