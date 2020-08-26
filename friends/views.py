from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class FriendsView(TemplateView, CategoryListMixin):
    template_name = "friends.html"
