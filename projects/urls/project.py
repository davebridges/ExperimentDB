from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^(?P<project>[-\w]+)/$', 'experimentdb.projects.views.detail', name="project-detail"),		
	url(r'^$', 'experimentdb.projects.views.index', name="project-list"),
)
