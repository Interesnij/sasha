from django.conf.urls import url
from appeal.views import *


urlpatterns = [
    url(r'^$', AppealView.as_view(), name='appeal'),
    url(r'^(?P<pk>\d+)/$', SurveyDetailView.as_view(), name="appeal_detail"),

    url(r'^vote/(?P<pk>\d+)/$', SurveyVoteCreate.as_view()),
    url(r'^unvote/(?P<pk>\d+)/$', SurveyVoteDelete.as_view()),
]
