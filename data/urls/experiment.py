from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import permission_required

from experimentdb.data.forms import ExperimentForm

urlpatterns = patterns('',
	url(r'^new/$', 'django.views.generic.create_update.create_object', {
		'form_class': ExperimentForm, 
		'template_name': 'experiment_form.html', 
		'login_required':True ,
		}, name="experiment-new"),
	url(r'^(?P<experimentID>[-\w]+)/$', 'experimentdb.data.views.experiment', name="experiment-detail),
	url(r'^(?P<experimentID>[-\w]+)/result/new/$', 'experimentdb.data.views.result_new', name="result-new"),
	url(r'^(?P<experimentID>[-\w]+)/edit/$', 'experimentdb.data.views.experiment_edit', name="experiment-edit"),
	url(r'^$', 'experimentdb.data.views.index', name="experiment-list"),
)
