from django.conf.urls.defaults import *

from experimentdb.data.forms import ExperimentForm

urlpatterns = patterns('',
	url(r'^(?P<subproject>[-\w]+)/$', 'experimentdb.projects.views.subproject_detail', name="subproject-detail"),
)
