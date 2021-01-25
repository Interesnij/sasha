import json
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from django.views.generic import ListView
from appeal.models import *
from django.views import View
from django.http import HttpResponse
from django.http import Http404


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

class SurveyDetailView(TemplateView, CategoryListMixin):
	template_name = "survey_detail.html"

	def get(self,request,*args,**kwargs):
		self.survey = Survey.objects.get(pk=self.kwargs["pk"])
		return super(SurveyDetailView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(SurveyDetailView,self).get_context_data(**kwargs)
		context["object"] = self.survey
		return context

class SurveyVote(View):
	def get(self, request, **kwargs):
		from datetime import datetime

		answer = Answer.objects.get(pk=self.kwargs["answer_pk"])
		user, survey = User.objects.get(pk=self.kwargs["pk"]), answer.survey
		if survey.time_end < datetime.now():
			return HttpResponse()
		try:
			answer = SurveyVote.objects.get(answer=answer, user=request.user)
			if survey.is_no_edited:
				return HttpResponse()
			else:
				answer.delete()
				result = True
		except SurveyVote.DoesNotExist:
			if not survey.is_multiple and request.user.is_voted_of_survey(survey.pk):
				request.user.get_vote_of_survey(survey.pk).delete()
			SurveyVote.objects.create(answer=answer, user=request.user)
			result = True
		return HttpResponse(json.dumps({"result": result,"votes": survey.get_votes_count()}), content_type="application/json")
