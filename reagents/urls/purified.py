from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.reagents.models import Purified_Protein

@login_required
def purified_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def purified_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_purified_protein')
def create_purified(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_purified_protein')
def change_purified(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_purified_protein')
def delete_purified(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', purified_list, {
		"queryset": Purified_Protein.objects.all(), 
		'template_name': 'purified_list.html',
		}, name="purified-list"),
	url(r'^(?P<object_id>[\d]+)/$', purified_detail, {
		"queryset": Purified_Protein.objects.all(), 
		'template_name': 'purified_detail.html'
		,}, name="purified-detail"),
	url(r'^new/$', create_purified, {
		'model': Purified_Protein, 
		'template_name': 'purified_form.html', 
		'login_required':True 
		}, name="purified-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_purified, {
		'model': Purified_Protein, 
		'template_name': 'purified_form.html',
		'login_required':True 
		,}, name="purified-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_purified, {
		'model': Purified_Protein, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/purified'
		,}, name="purified-delete"),
)
