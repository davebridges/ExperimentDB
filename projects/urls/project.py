'''This package is the url redirection for the projects app.'''

from django.conf.urls import *

from projects import views


urlpatterns = patterns('',
	url(r'^new/$', views.ProjectCreate.as_view(), name="project-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.ProjectDetail.as_view(), name="project-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.ProjectUpdate.as_view(), name="project-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.ProjectDelete.as_view(), name="project-delete"),
    url(r'^$', views.ProjectList.as_view(), name="project-list"),
)
