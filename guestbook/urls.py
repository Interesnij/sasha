from django.conf.urls import url
from guestbook.views import AboutView


urlpatterns = [
    url(r'^$', GuestbookView.as_view(), name='guestbook'),
]
