from django.conf.urls import url
from auths.views import AuthView


urlpatterns = [
    url(r'^$', AuthView.as_view(), name='auth'),
]
