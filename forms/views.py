from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class FormsView(TemplateView, CategoryListMixin):
    template_name = "forms.html"
