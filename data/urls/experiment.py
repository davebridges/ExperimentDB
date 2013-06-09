from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required

from data.forms import ExperimentForm

from data import views

urlpatterns = patterns('',
	url(r'^new/$', views.ExperimentCreate.as_view(), name="experiment-new"),
	url(r'^(?P<experimentID>[-\w]+)/$', 'data.views.experiment', name="experiment-detail"),
	url(r'^(?P<experimentID>[-\w]+)/result/new/$', 'data.views.result_new', name="result-new"),
	url(r'^(?P<slug>[-\w]+)/edit/$', views.ExperimentEdit.as_view(), name="experiment-edit"),
	url(r'^$', 'data.views.index', name="experiment-list"),
)
