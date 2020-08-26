from django.conf.urls import url
from forms.views import FormsView


urlpatterns = [
    url(r'^$', FormsView.as_view(), name='forms'),
]
