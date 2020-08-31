from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from users.models import User
from django.http import Http404
from users.forms import UserForm


class UserView(TemplateView, CategoryListMixin):
	template_name = "user.html"

	def get(self,request,*args,**kwargs):
		self.user = User.objects.get(pk=self.kwargs["pk"])
		return super(UserView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(UserView,self).get_context_data(**kwargs)
		context["user"] = self.user
		return context


class UserSettings(TemplateView):
	template_name = "user_settings.html"
	form = None

	def get(self,request,*args,**kwargs):
		self.user = User.objects.get(pk=self.kwargs["pk"])
		return super(UserSettings,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(UserSettings,self).get_context_data(**kwargs)
		context["form"] = UserForm()
		return context

	def post(self,request,*args,**kwargs):
		self.form = UserForm(request.POST, instance=self.user)
		if self.form.is_valid():
			user = self.request.user
			self.form.save()
			return redirect('user', pk=self.user.pk)
		return super(UserSettings,self).post(request,*args,**kwargs)
