from django.conf.urls import url
from movies.views import MoviesView


urlpatterns = [
    url(r'^$', MoviesView.as_view(), name='movies'),
]
