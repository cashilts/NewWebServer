from django.conf.urls import url

from . import views

app_name="projects"
urlpatterns = [
	url(r'^$', views.index, name='projects'),
	url(r'^add/$', views.add, name='add'),
	url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^submit/$', views.submit, name='submit'),
]
