from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.reagents.models import Antibody

@login_required
def antibody_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def antibody_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_antibody')
def create_antibody(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_antibody')
def change_antibody(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_antibody')
def delete_antibody(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', antibody_list, {
		"queryset": Antibody.objects.all(), 
		'template_name': 'antibody_list.html',
		}, name="antibody-list"),
	url(r'^(?P<object_id>[\d]+)/$', antibody_detail, {
		"queryset": Antibody.objects.all(), 
		'template_name': 'antibody_detail.html'
		,}, name="antibody-detail"),
	url(r'^new/$', create_antibody, {
		'model': Antibody, 
		'template_name': 'antibody_form.html', 
		'login_required':True 
		}, name="antibody-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_antibody, {
		'model': Antibody, 
		'template_name': 'antibody_form.html',
		'login_required':True 
		,}, name="antibody-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_antibody, {
		'model': Antibody, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/antibody'
		,}, name="antibody-delete"),
	url(r'^lookup/$', 'experimentdb.reagents.views.antibody_lookup', name="antibody-lookup")
)
