from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.reagents.models import Primer

@login_required
def primer_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def primer_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_primer')
def create_primer(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_primer')
def change_primer(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_primer')
def delete_primer(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', primer_list, {
		"queryset": Primer.objects.all(), 
		'template_name': 'primer_list.html',
		}, name="primer-list"),
	url(r'^(?P<object_id>[\d]+)/$', primer_detail, {
		"queryset": Primer.objects.all(), 
		'template_name': 'primer_detail.html'
		,}, name="primer-detail"),
	url(r'^new/$', create_primer, {
		'model': Primer, 
		'template_name': 'primer_form.html', 
		'login_required':True ,
		}, name="primer-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_primer, {
		'model': Primer, 
		'template_name': 'primer_form.html',
		'login_required':True 
		,}, name="primer-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_primer, {
		'model': Primer, 
		'login_required':True,
		'template_name': 'confirm_delete.html',
		'post_delete_redirect': '/experimentdb/primer',
		}, name="primer-delete"),
)
