from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class MoviesView(TemplateView, CategoryListMixin):
    template_name = "movies.html"
