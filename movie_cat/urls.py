from django.conf.urls import url
from movie_cat.views import MovieCatView


urlpatterns = [
    url(r'^$', MovieCatView.as_view(), name='movie_cat'),
]
