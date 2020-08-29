from proects.views import ProectsListView, ProectView
from django.conf.urls import url


urlpatterns = [
	url(r'^$', ProectsListView.as_view(), name="proects_index"),
	url(r'^(?P<slug>[\w\-]+)/$', ProectView.as_view(), name="proect_detail"),
]
