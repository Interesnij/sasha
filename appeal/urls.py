from django.conf.urls import url
from appeal.views import *


urlpatterns = [
    url(r'^$', AppealView.as_view(), name='appeal'),
    url(r'^(?P<pk>\d+)/$', AppealDetailView.as_view(), name="appeal_detail"),
    url(r'^a(?P<pk>\d+)/$', SurveyDetailView.as_view(), name="survey_detail"),

    url(r'^vote/(?P<pk>\d+)/(?P<answer_pk>\d+)/$', SurveyVote),
]
