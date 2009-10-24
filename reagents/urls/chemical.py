from django.conf.urls.defaults import *

from experimentdb.reagents.models import Chemical

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', {
		"queryset": Chemical.objects.all(), 
		'template_name': 'chemical_list.html',
		}),
	(r'^(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Chemical.objects.all(), 
		'template_name': 'chemical_detail.html'
		,}),
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': Chemical, 
		'template_name': 'chemical_form.html', 
		'login_required':True 
		}),	
)
