from django.conf.urls import url
from appeal.views import *


urlpatterns = [
    url(r'^$', AppealView.as_view(), name='appeal'),
    url(r'^(?P<pk>\d+)/$',AppealDetailView.as_view(), name="appeal_detail"),

    url(r'^like/(?P<pk>\d+)/$',AppealLikeCreate.as_view()),
]
