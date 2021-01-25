import json
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from django.views.generic import ListView
from appeal.models import *
from users.models import User
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

class SurveyVoteCreate(View):
	template_name = None

	def post(self,request,*args,**kwargs):
		from appeal.forms import UserForm

		form = UserForm(request.POST)
		survey = Survey.objects.get(pk=self.kwargs["pk"])
		if request.is_ajax() and form.is_valid():
			answers = request.POST.getlist("answers")
			if not answers:
				return HttpResponse("not ansvers")
			region = request.POST.get("region")
			for answer in answers:
				SurveyVote.objects.create(answer_id=answer, user=requset.user)
			if region:
				user = User.objects.get(pk=requset.user.pk)
				user.region = region
				user.save()
			return HttpResponse()
		return HttpResponse()
