from django.conf.urls import url
from friends.views import FriendsView


urlpatterns = [
    url(r'^$', FriendsView.as_view(), name='friends'),
]
