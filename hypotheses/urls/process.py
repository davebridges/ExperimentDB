from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.hypotheses.models import Process

@login_required
def process_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def process_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_process')
def create_process(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_process')
def change_process(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_process')
def delete_process(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', process_list, {
		"queryset": Process.objects.all(), 
		'template_name': 'process_list.html',
		}, name="process-list"),
	url(r'^(?P<object_id>[\d]+)/$', process_detail, {
		"queryset": Process.objects.all(), 
		'template_name': 'process_detail.html'
		,}, name="process-detail"),
	url(r'^new/$', create_process, {
		'model': Process, 
		'template_name': 'process_form.html', 
		'login_required':True 
		}, name="process-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_process, {
		'model': Process, 
		'template_name': 'process_form.html',
		'login_required':True 
		,}, name="process-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_process, {
		'model': Process, 
		'login_required':True,
		'template_name': 'confirm_delete.html',
		'post_delete_redirect': '/experimentdb/process'
		,}, name="process-delete"),
)
