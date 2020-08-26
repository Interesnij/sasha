from django.conf.urls import url
from friends.views import AboutView


urlpatterns = [
    url(r'^$', FriendsView.as_view(), name='friends'),
]
