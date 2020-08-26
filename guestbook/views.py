from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class GuestbookView(TemplateView, CategoryListMixin):
    template_name = "guestbook.html"
