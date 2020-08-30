from django.conf.urls import url
from movie_cat.views import MovieListView


urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/$', MovieListView.as_view(), name='movies_index'),
]
