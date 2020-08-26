from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class MovieCatView(TemplateView, CategoryListMixin):
    template_name = "movie_cat.html"
