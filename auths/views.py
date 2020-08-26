from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class AuthView(TemplateView, CategoryListMixin):
    template_name = "auth.html"
