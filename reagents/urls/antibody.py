from django.conf.urls.defaults import *

from experimentdb.reagents.models import Antibody

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', {
		"queryset": Antibody.objects.all(), 
		'template_name': 'antibody_list.html',
		}),
	(r'^(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Antibody.objects.all(), 
		'template_name': 'antibody_detail.html'
		,}),
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': Antibody, 
		'template_name': 'antibody_form.html', 
		'login_required':True 
		}),
	(r'^(?P<object_id>[\d]+)/edit$', 'django.views.generic.create_update.update_object', {
		'model': Antibody, 
		'template_name': 'antibody_form.html',
		'login_required':True 
		,}),
	(r'^(?P<object_id>[\d]+)/delete$', 'django.views.generic.create_update.delete_object', {
		'model': Antibody, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/antibody'
		,}),
)
