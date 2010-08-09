from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.projects.models import Project

@login_required
def project_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def project_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('projects.add_project')
def create_project(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('projects.change_project')
def change_project(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('projects.delete_project')
def delete_project(*args, **kwargs):
	return delete_object(*args, **kwargs)


urlpatterns = patterns('',
	url(r'^$', project_list, {
		"queryset": Project.objects.all(), 
		'template_name': 'project_list.html',
		}, name="project-list"),
	url(r'^(?P<object_id>[\d]+)/$', project_detail, {
		"queryset": Project.objects.all(), 
		'template_name': 'project_detail.html'
		,}, name="project-detail"),
	url(r'^new/$', create_project, {
		'model': Project, 
		'template_name': 'project_form.html', 
		'login_required':True 
		}, name="project-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_project, {
		'model': Project, 
		'template_name': 'project_form.html',
		'login_required':True 
		,}, name="project-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_project, {
		'model': Project, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/project'
		,}, name="project-delete"),
)
