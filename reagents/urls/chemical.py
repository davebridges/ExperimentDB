from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.reagents.models import Chemical

@login_required
def chemical_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def chemical_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_chemical')
def create_chemical(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_chemical')
def change_chemical(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_chemical')
def delete_chemical(*args, **kwargs):
	return delete_object(*args, **kwargs)

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
		(r'^(?P<object_id>[\d]+)/edit$', 'django.views.generic.create_update.update_object', {
		'model': Chemical, 
		'template_name': 'chemical_form.html',
		'login_required':True 
		,}),
	(r'^(?P<object_id>[\d]+)/delete$', 'django.views.generic.create_update.delete_object', {
		'model': Chemical, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/chemical'
		,}),
)
