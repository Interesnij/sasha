from django.conf.urls import url
from users.views import UserView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', UserView.as_view(), name='user'),
]
