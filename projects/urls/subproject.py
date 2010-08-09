from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.projects.models import SubProject

@login_required
def subproject_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def subproject_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('projects.add_subproject')
def create_subproject(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('projects.change_subproject')
def change_subproject(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('projects.delete_subproject')
def delete_subproject(*args, **kwargs):
	return delete_object(*args, **kwargs)


urlpatterns = patterns('',
	url(r'^$', subproject_list, {
		"queryset": SubProject.objects.all(), 
		'template_name': 'subproject_list.html',
		}, name="subproject-list"),
	url(r'^(?P<object_id>[\d]+)/$', subproject_detail, {
		"queryset": SubProject.objects.all(), 
		'template_name': 'subproject_detail.html'
		,}, name="subproject-detail"),
	url(r'^new/$', create_subproject, {
		'model': SubProject, 
		'template_name': 'subproject_form.html', 
		'login_required':True 
		}, name="subproject-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_subproject, {
		'model': SubProject, 
		'template_name': 'subproject_form.html',
		'login_required':True 
		,}, name="subproject-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_subproject, {
		'model': SubProject, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/subproject'
		,}, name="subproject-delete"),
)
