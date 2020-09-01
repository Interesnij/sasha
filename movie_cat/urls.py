from django.conf.urls import url
from movie_cat.views import MovieListView, MovieLists


urlpatterns = [
    url(r'^(?P<slug>[\w\-]+)/$', MovieListView.as_view(), name='movies_index'),
    url(r'^playlists/$', MovieLists.as_view(), name='movies_list'),
]
