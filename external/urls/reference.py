"""This file contains the url redirections for reference objects.

This includes generic create, update, delete, detail and list pages."""

from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import permission_required, login_required

from external.models import Reference

from external import views

@login_required
def reference_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def reference_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('external.add_reference')
def create_reference(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('external.change_reference')
def change_reference(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('external.delete_reference')
def delete_reference(*args, **kwargs):
	return delete_object(*args, **kwargs)


urlpatterns = patterns('',
	url(r'^$', views.PaperListView.as_view(), name="reference-list"),
	url(r'^lab-papers/?$', views.LaboratoryPaperListView.as_view, name='lab-reference-list'),
	url(r'^interesting-papers/?$', views.InterestingPaperListView.as_view, name='lab-reference-list'),
    url(r'^(?P<title_slug>[-\w]+)/$', views.PaperDetailView.as_view(), name="paper-details"), 		
	url(r'^new/$', create_reference, {
		'model': Reference, 
		'template_name': 'reference_form.html', 
		'login_required':True 
		}, name="reference-new"),
	url(r'^(?P<id>[\w]+)/edit$', change_reference, {
		'model': Reference, 
		'template_name': 'reference_form.html',
		'login_required':True,	
		}, name="reference-edit"),
	url(r'^(?P<id>[\d]+)/delete$', delete_reference, {
		'model': Reference, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/reference'
		}, name="reference-delete"),
)
