from django.conf.urls import url
from auth.views import AboutView


urlpatterns = [
    url(r'^$', AuthView.as_view(), name='auth'),
]
