from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from usersignup import views

urlpatterns = [	
    url(r'^logout/$', auth_views.logout, {'next_page': 'usersignup:login'}, name='logout'),
	url(r'^signup/$',views.signup, name='signup'),
	url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
]