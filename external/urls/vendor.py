"""This file contains the url redirections for vendor objects.

This includes generic create, update, delete, detail and list pages."""

from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import permission_required, login_required

from experimentdb.external.models import Vendor

@login_required
def vendor_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def vendor_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('external.add_vendor')
def create_vendor(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('external.change_vendor')
def change_vendor(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('external.delete_vendor')
def delete_vendor(*args, **kwargs):
	return delete_object(*args, **kwargs)


urlpatterns = patterns('',
	url(r'^$', vendor_list, {
		"queryset": Vendor.objects.all(), 
		'template_name': 'vendor_list.html',
		'template_object_name': 'vendor'
		}, name="vendor-list"),
	url(r'^(?P<id>[\d]+)/$', vendor_detail, {
		"queryset": Vendor.objects.all(), 
		'template_name': 'vendor_detail.html',
		'template_object_name': 'vendor',
		}, name="vendor-detail"),
	url(r'^new/$', create_vendor, {
		'model': Vendor, 
		'template_name': 'vendor_form.html', 
		'login_required':True 
		}, name="vendor-new"),
	url(r'^(?P<id>[\w]+)/edit$', change_vendor, {
		'model': Vendor, 
		'template_name': 'vendor_form.html',
		'login_required':True,	
		}, name="vendor-edit"),
	url(r'^(?P<id>[\d]+)/delete$', delete_vendor, {
		'model': Vendor, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/vendor'
		}, name="vendor-delete"),
)
