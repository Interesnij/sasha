from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include ('main.urls')),

    url(r'^movie_cat/', include('movie_cat.urls')),
    url(r'^movies/', include('movies.urls')),

    url(r'^blog_cat/', include('blog_cat.urls')),
    url(r'^blog/', include('blog.urls')),

    url(r'^forms/', include('forms.urls')),

    url(r'^proects/', include('proects.urls')),
    url(r'^friends/', include('friends.urls')),

    url(r'^search/', include('search.urls')),
    url(r'^users/', include('users.urls')),

    url(r'^about/', include('about.urls')),
    url(r'^contacts/', include('contacts.urls')),

    url(r'^terms/', include('terms.urls')),
    url(r'^policy/', include('policy.urls')),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^signup/$', TemplateView.as_view(template_name="account/signup.html"), name='signup'),
    url(r'^login/$', TemplateView.as_view(template_name="account/login.html"), name='login'),
    url(r'^email-verification/$', TemplateView.as_view(template_name="account/email_verification.html"), name='email-verification'),
    url(r'^password-reset/$',TemplateView.as_view(template_name="account/password_reset.html"), name='password-reset'),
    url(r'^password-reset/confirm/$',TemplateView.as_view(template_name="account/password_reset_confirm.html"), name='password-reset-confirm'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', TemplateView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^password-change/$',TemplateView.as_view(template_name="account/password_change.html"), name='password-change'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    url(r'^account/', include('allauth.urls')),

]  +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
