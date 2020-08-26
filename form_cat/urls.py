from django.conf.urls import url
from form_cat.views import FormCatView


urlpatterns = [
    url(r'^$', FormCatView.as_view(), name='form_cat'),
]
