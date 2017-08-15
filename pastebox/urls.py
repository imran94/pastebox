from django.conf.urls import url, include
from . import views

app_name = 'pastebox'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^search/', views.search, name='search'),
	url(r'^(?P<post_url>[a-zA-z0-9]{8})/$', views.detail, name='detail'),
	url(r'^(?P<post_url>[a-zA-z0-9]{8})/delete/$', views.delete, name='delete'),
	url(r'^save/$', views.save, name='save')
]