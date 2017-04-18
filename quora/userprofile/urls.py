from django.conf.urls import url
from .views import profile,home
# from .views import Temp

urlpatterns=[
	url(r'^profilecreate/$',profile,name='profilecreate'),
	url(r'^home/$',home,name='home'),
	# url(r'^temp/$',Temp.as_view(),)


]