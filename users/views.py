from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class UsersView(TemplateView, CategoryListMixin):
    template_name = "users.html"
