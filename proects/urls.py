from django.conf.urls import url
from proects.views import ProectsView


urlpatterns = [
    url(r'^$', ProectsView.as_view(), name='proects'),
]
