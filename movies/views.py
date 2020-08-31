import json
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from movies.models import Video, VideoComment
from movies.forms import CommentForm
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.views.generic import ListView


class MovieDetailView(TemplateView):
	template_name = "movie.html"

	def get(self,request,*args,**kwargs):
		self.video = Video.objects.get(slug=self.kwargs["slug"])
		return super(MovieDetailView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(MovieDetailView,self).get_context_data(**kwargs)
		context["object"] = self.video
		return context


class VideoCommentList(ListView):
    template_name = "comments.html"
    paginate_by = 15

    def get(self,request,*args,**kwargs):
        self.video = Video.objects.get(pk=self.kwargs["pk"])
        return super(VideoCommentList,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(VideoCommentList, self).get_context_data(**kwargs)
        context['parent'] = self.video
        return context

    def get_queryset(self):
        comments = self.video.get_comments()
        return comments


class VideoCommentCreate(View):

    def post(self,request,*args,**kwargs):
        form_post = CommentForm(request.POST)
        video_comment = Video.objects.get(pk=request.POST.get('pk'))

        if request.is_ajax() and form_post.is_valid() and video_comment.comments_enabled:
            comment = form_post.save(commit=False)
            new_comment = comment.create_comment(commenter=request.user, parent_comment=None, video_comment=video_comment, text=comment.text)
            return render(request, 'video_comment.html',{'comment': new_comment})
        else:
            return HttpResponseBadRequest()


class VideoReplyCreate(View):
    def post(self,request,*args,**kwargs):
        form_post = CommentForm(request.POST)
        parent = VideoComment.objects.get(pk=request.POST.get('video_comment'))

        if request.is_ajax() and form_post.is_valid() and parent.video_comment.comments_enabled:
            comment = form_post.save(commit=False)
            new_comment = comment.create_comment(commenter=request.user, parent_comment=parent, video_comment=None, text=comment.text)
            return render(request, 'video_reply_comment.html',{'reply': new_comment, 'comment': parent,})
        else:
            return HttpResponseBadRequest()

class VideoCommentDelete(View):
    def get(self,request,*args,**kwargs):
        comment = VideoComment.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.pk == comment.commenter.pk:
            comment.is_deleted = True
            comment.save(update_fields=['is_deleted'])
            return HttpResponse()
        else:
            raise Http404

class VideoCommentAbortDelete(View):
    def get(self,request,*args,**kwargs):
        comment = VideoComment.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.pk == comment.commenter.pk:
            comment.is_deleted = False
            comment.save(update_fields=['is_deleted'])
            return HttpResponse()
        else:
            raise Http404


class VideoLikeCreate(View):
    def get(self, request, **kwargs):
        video = Video.objects.get(uuid=self.kwargs["uuid"])
        if not request.is_ajax() and not video.votes_on:
            raise Http404
        try:
            likedislike = VideoVotes.objects.get(parent=video, user=request.user)
            if likedislike.vote is not VideoVotes.LIKE:
                likedislike.vote = VideoVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoVotes.DoesNotExist:
            VideoVotes.objects.create(parent=video, user=request.user, vote=VideoVotes.LIKE)
            result = True
        likes = video.likes_count()
        if likes != 0:
            like_count = likes
        else:
            like_count = ""
        dislikes = video.dislikes_count()
        if dislikes != 0:
            dislike_count = dislikes
        else:
            dislike_count = ""
        return HttpResponse(json.dumps({"result": result,"like_count": str(like_count),"dislike_count": str(dislike_count)}),content_type="application/json")


class VideoCommentLikeCreate(View):
    def get(self, request, **kwargs):
        comment = VideoComment.objects.get(pk=self.kwargs["comment_pk"])
        if not request.is_ajax():
            raise Http404
        try:
            likedislike = VideoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not VideoCommentVotes.LIKE:
                likedislike.vote = VideoCommentVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoCommentVotes.DoesNotExist:
            VideoCommentVotes.objects.create(item=comment, user=request.user, vote=VideoCommentVotes.LIKE)
            result = True
        likes = comment.likes_count()
        if likes != 0:
            like_count = likes
        else:
            like_count = ""
        dislikes = comment.dislikes_count()
        if dislikes != 0:
            dislike_count = dislikes
        else:
            dislike_count = ""
        return HttpResponse(json.dumps({"result": result,"like_count": str(like_count),"dislike_count": str(dislike_count)}),content_type="application/json")


class VideoDislikeCreate(View):
    def get(self, request, **kwargs):
        video = Video.objects.get(uuid=self.kwargs["uuid"])
        if not request.is_ajax() and not video.votes_on:
            raise Http404
        try:
            likedislike = VideoVotes.objects.get(parent=video, user=request.user)
            if likedislike.vote is not VideoVotes.DISLIKE:
                likedislike.vote = VideoVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoVotes.DoesNotExist:
            VideoVotes.objects.create(parent=video, user=request.user, vote=VideoVotes.DISLIKE)
            result = True
        likes = item.likes_count()
        if likes != 0:
            like_count = likes
        else:
            like_count = ""
        dislikes = video.dislikes_count()
        if dislikes != 0:
            dislike_count = dislikes
        else:
            dislike_count = ""
        return HttpResponse(json.dumps({"result": result,"like_count": str(like_count),"dislike_count": str(dislike_count)}),content_type="application/json")


class VideoCommentDislikeCreate(View):
    def get(self, request, **kwargs):
        comment = VideoComment.objects.get(pk=self.kwargs["comment_pk"])
        if not request.is_ajax():
            raise Http404
        try:
            likedislike = VideoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not VideoCommentVotes.DISLIKE:
                likedislike.vote = VideoCommentVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoCommentVotes.DoesNotExist:
            VideoCommentVotes.objects.create(item=comment, user=request.user, vote=VideoCommentVotes.DISLIKE)
            result = True
        likes = comment.likes_count()
        if likes:
            like_count = likes
        else:
            like_count = ""
        dislikes = comment.dislikes_count()
        if dislikes != 0:
            dislike_count = dislikes
        else:
            dislike_count = ""
        return HttpResponse(json.dumps({"result": result,"like_count": str(like_count),"dislike_count": str(dislike_count)}),content_type="application/json")
