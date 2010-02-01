from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import permission_required

from experimentdb.data.forms import ExperimentForm

urlpatterns = patterns('',
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'form_class': ExperimentForm, 
		'template_name': 'experiment_form.html', 
		'login_required':True ,
		}),
	(r'^(?P<experimentID>[-\w]+)/$', 'experimentdb.data.views.experiment'),
	(r'^(?P<experimentID>[-\w]+)/result/new/$', 'experimentdb.data.views.result_new'),
	(r'^(?P<experimentID>[-\w]+)/edit/$', 'experimentdb.data.views.experiment_edit'),
	(r'^$', 'experimentdb.data.views.index'),
)
