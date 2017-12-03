from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^data/', views.ind, name='ind'),
	url(r'^give/', views.req, name='req'),
]