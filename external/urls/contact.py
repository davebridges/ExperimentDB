"""This file contains the url redirections for contact objects.

This includes generic create, update, delete, detail and list pages."""

from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import permission_required, login_required

from experimentdb.external.models import Contact

@login_required
def contact_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def contact_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('external.add_contact')
def create_contact(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('external.change_contact')
def change_contact(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('external.delete_contact')
def delete_contact(*args, **kwargs):
	return delete_object(*args, **kwargs)


urlpatterns = patterns('',
	url(r'^$', contact_list, {
		"queryset": Contact.objects.all(), 
		'template_name': 'contact_list.html',
		'template_object_name': 'contact'
		}, name="contact-list"),
	url(r'^(?P<id>[\d]+)/$', contact_detail, {
		"queryset": Contact.objects.all(), 
		'template_name': 'contact_detail.html',
		'template_object_name': 'contact',
		}, name="contact-detail"),
	url(r'^new/$', create_contact, {
		'model': Contact, 
		'template_name': 'contact_form.html', 
		'login_required':True 
		}, name="contact-new"),
	url(r'^(?P<id>[\w]+)/edit$', change_contact, {
		'model': Contact, 
		'template_name': 'contact_form.html',
		'login_required':True,	
		}, name="contact-edit"),
	url(r'^(?P<id>[\d]+)/delete$', delete_contact, {
		'model': Contact, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/contact'
		}, name="contact-delete"),
)
