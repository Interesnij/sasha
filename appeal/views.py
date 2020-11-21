from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from django.views.generic import ListView
from appeal.models import Appeal


class AppealView(ListView, CategoryListMixin):
	template_name = "appeal_index.html"
	paginate_by = 15

	def get_queryset(self):
		appeals = Appeal.objects.only("pk")
		return appeals


class AppealDetailView(TemplateView, CategoryListMixin):
	template_name = "appeal_detail.html"

	def get(self,request,*args,**kwargs):
		self.appeal = Appeal.objects.get(pk=self.kwargs["pk"])
		return super(AppealDetailView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(AppealDetailView,self).get_context_data(**kwargs)
		context["object"] = self.appeal
		return context


class AppealLikeCreate(View):
    def get(self, request, **kwargs):
        appeal = Appeal.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax():
            raise Http404
        try:
            likedislike = AppealVotes.objects.get(parent=appeal, user=request.user)
            if likedislike.vote is not AppealVotes.LIKE:
                likedislike.vote = AppealVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except AppealVotes.DoesNotExist:
            AppealVotes.objects.create(parent=appeal, user=request.user, vote=AppealVotes.LIKE)
            result = True
        likes = appeal.likes_count()
        if likes != 0:
            like_count = likes
        else:
            like_count = ""
        return HttpResponse(json.dumps({"result": result,"like_count": str(like_count)}),content_type="application/json")
