from django.conf.urls import url
from blog.views import BlogView


urlpatterns = [
    url(r'^$', BlogView.as_view(), name='blog'),
]
