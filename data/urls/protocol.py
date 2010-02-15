"""This module provides url direction for protocol pages.

Generic pages are used for all views.  Pages are located at /experimentdb/protocol/##/(new/edit/delete).
Restrictions are placed on list/detail pages for login and appropriate permissions for add/edit/delete pages.
"""

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.data.models import Protocol

@login_required
def protocol_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def protocol_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('data.add_protocol')
def create_protocol(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('data.change_protocol')
def change_protocol(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('data.delete_protocol')
def delete_protocol(*args, **kwargs):
	return delete_object(*args, **kwargs)


urlpatterns = patterns('',
	url(r'^$', protocol_list, {
		"queryset": Protocol.objects.all(), 
		'template_name': 'protocol_list.html',
		}, name="protocol-list"),
	url(r'^(?P<object_id>[\d]+)/$', protocol_detail, {
		"queryset": Protocol.objects.all(), 
		'template_name': 'protocol_detail.html'
		,}, name="protocol-detail"),
	url(r'^new/$', create_protocol, {
		'model': Protocol, 
		'template_name': 'protocol_form.html', 
		'login_required':True ,
		}, name="protocol-new"),
	url(r'^(?P<object_id>[-\d]+)/edit/$', change_protocol, {
		'model': Protocol, 
		'template_name': 'protocol_form.html',
		'login_required':True 
		,}, name="protocol-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_protocol, {
		'model': Protocol, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/protocol'
		,}, name="protocol-delete"),
)
