from django.conf.urls.defaults import *

from experimentdb.data.forms import ExperimentForm

urlpatterns = patterns('',
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'form_class': ExperimentForm, 
		'template_name': 'experiment_form.html', 
		'login_required':True ,
		'post_save_redirect': 'object.get_absolute_url()'
		}),
	(r'^(?P<experimentID>[-\w]+)/$', 'experimentdb.data.views.experiment'),
	(r'^(?P<experimentID>[-\w]+)/result/new/$', 'experimentdb.data.views.result_new'),
	(r'^(?P<experimentID>[-\w]+)/edit/$', 'experimentdb.data.views.experiment_edit'),
	(r'^$', 'experimentdb.data.views.index'),
)
