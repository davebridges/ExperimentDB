from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.reagents.models import Cell

@login_required
def cell_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def cell_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_cell')
def create_cell(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_cell')
def change_cell(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_cell')
def delete_cell(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', cell_list, {
		"queryset": Cell.objects.all(), 
		'template_name': 'cell_list.html',
		}, name="cell-list"),
	url(r'^(?P<object_id>[\d]+)/$', cell_detail, {
		"queryset": Cell.objects.all(), 
		'template_name': 'cell_detail.html'
		,}, name="cell-detail"),
	url(r'^new/$', create_cell, {
		'model': Cell, 
		'template_name': 'cell_form.html', 
		'login_required':True 
		}, name="cell-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_cell, {
		'model': Cell, 
		'template_name': 'cell_form.html',
		'login_required':True 
		,}, name="cell-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_cell, {
		'model': Cell, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/cell'
		,}, name="cell-delete"),
)
