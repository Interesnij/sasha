from django.conf.urls import url
from blog_cat.views import BlogCatView


urlpatterns = [
    url(r'^$', BlogCatView.as_view(), name='blog_cat'),
]
