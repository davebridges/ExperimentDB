from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.reagents.models import Strain

@login_required
def strain_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def strain_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_strain')
def create_strain(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_strain')
def change_strain(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_strain')
def delete_strain(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', strain_list, {
		"queryset": Strain.objects.all(), 
		'template_name': 'strain_list.html',
		}, name="strain-list"),
	url(r'^(?P<object_id>[\d]+)/$', strain_detail, {
		"queryset": Strain.objects.all(), 
		'template_name': 'strain_detail.html'
		,}, name="strain-detail"),
	url(r'^new/$', create_strain, {
		'model': Strain, 
		'template_name': 'strain_form.html', 
		'login_required':True 
		}, name="strain-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_strain, {
		'model': Strain,
		'template_name': 'strain_form.html',
		'login_required':True 
		,}, name="strain-edit"),
	url(r'^(?P<object_id>[\d]+)/update$', change_strain, {
		'model': Strain,
		'template_name': 'strain_form.html',
		'login_required':True 
		,}),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_strain, {
		'model': Strain,
		'template_name': 'confirm_delete.html',
		'login_required':True ,
		'post_delete_redirect': "/experimentdb/strain"
		,}, name="strain-delete"),
)
