from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required

from data.forms import ExperimentForm

from data import views

urlpatterns = patterns('',
	url(r'^new/$', views.ExperimentCreate.as_view(), name="experiment-new"),
	url(r'^(?P<experimentID>[-\w]+)/$', 'data.views.experiment', name="experiment-detail"),
	url(r'^(?P<experimentID>[-\w]+)/raw-data/new/$', 'data.views.raw_data_file_new', name="raw-data-file-new"),
        url(r'^(?P<experimentID>[-\w]+)/figure/new/$', 'data.views.figure_file_new', name="figure-file-new"),	
        url(r'^(?P<slug>[-\w]+)/edit/$', views.ExperimentEdit.as_view(), name="experiment-edit"),
	url(r'^$', 'data.views.index', name="experiment-list"),
)
