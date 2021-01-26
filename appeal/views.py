import json
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from django.views.generic import ListView
from appeal.models import *
from users.models import User
from django.views import View
from django.http import HttpResponse, Http404, JsonResponse


class AppealView(ListView, CategoryListMixin):
	template_name = "appeal_index.html"
	paginate_by = 15

	def get_queryset(self):
		appeals = Appeal.objects.only("pk")
		return appeals

class SurveyDetailView(TemplateView, CategoryListMixin):
	template_name = "survey_detail.html"

	def get(self,request,*args,**kwargs):
		self.survey = Survey.objects.get(pk=self.kwargs["pk"])
		return super(SurveyDetailView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(SurveyDetailView,self).get_context_data(**kwargs)
		context["object"] = self.survey
		return context


class SurveyVoteCreate(View):
	def post(self,request,*args,**kwargs):
		from appeal.forms import UserForm

		form = UserForm(request.POST)
		survey = Survey.objects.get(pk=self.kwargs["pk"])
		if request.is_ajax() and form.is_valid():
			user = form.save(commit=False)
			answers = request.POST.getlist("answers")
			if not answers:
				return HttpResponse("not ansvers")
			region = request.POST.get("region")
			for answer in answers:
				SurveyVote.objects.create(answer_id=answer, user=request.user)
			if region:
				user = User.objects.get(pk=request.user.pk)
				user.region = region
				user.save()
			return HttpResponse()
		return HttpResponse()


class SurveyVoteDelete(View):
	def get(self,request,*args,**kwargs):
		survey = Survey.objects.get(pk=self.kwargs["pk"])
		if request.is_ajax():
			survey.remove_user_vote(request.user.pk)
			return HttpResponse()
		return HttpResponse()
