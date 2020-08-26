from django.conf.urls import url
from users.views import UsersView


urlpatterns = [
    url(r'^$', UsersView.as_view(), name='users'),
]
