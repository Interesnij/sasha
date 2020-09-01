from django.conf.urls import url
from about.views import AboutView


urlpatterns = [
    url(r'^$', AboutView.as_view(), name='about'),
    url(r'send_message/^$', FeedbackFormView.as_view()),
]
