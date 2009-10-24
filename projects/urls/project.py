from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^(?P<project>[-\w]+)/$', 'experimentdb.projects.views.detail'),		
	(r'^$', 'experimentdb.projects.views.index'),
)
