from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class FormCatView(TemplateView, CategoryListMixin):
    template_name = "form_cat.html"
