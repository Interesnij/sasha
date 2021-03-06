from django.conf.urls import url
from movies.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^(?P<pk>\d+)/$',MovieDetailView.as_view(), name="movies_detail"),

    url(r'^like/(?P<pk>\d+)/$',login_required(VideoLikeCreate.as_view())),
    url(r'^dislike/(?P<pk>\d+)/$',login_required(VideoDislikeCreate.as_view())),
    url(r'^comment_like/(?P<comment_pk>\d+)/$',login_required(VideoCommentLikeCreate.as_view())),
    url(r'^comment_dislike/(?P<comment_pk>\d+)/$',login_required(VideoCommentDislikeCreate.as_view())),

    url(r'^post-comment/$', login_required(VideoCommentCreate.as_view())),
    url(r'^reply-comment/$', login_required(VideoReplyCreate.as_view())),
    url(r'^delete_comment/(?P<pk>\d+)/$', login_required(VideoCommentDelete.as_view())),
    url(r'^abort_delete_comment/(?P<pk>\d+)/$', login_required(VideoCommentAbortDelete.as_view())),
    url(r'^comment/(?P<pk>\d+)/$', VideoCommentList.as_view()),
]
