from django.conf.urls import url, include
from . import views

app_name = 'pastebox'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<post_url>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<post_url>[0-9]+)/delete/$', views.delete, name='delete'),
	url(r'^search/', views.search, name='search'),
	url(r'^save/$', views.save, name='save')
]