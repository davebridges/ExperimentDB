from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.reagents.models import Construct

@login_required
def construct_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def construct_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_construct')
def create_construct(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_construct')
def change_construct(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_construct')
def delete_construct(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', construct_list, {
		"queryset": Construct.objects.all(), 
		'template_name': 'construct_list.html',
		}, name="construct-list"),
	url(r'^(?P<object_id>[\d]+)/$', construct_detail, {
		"queryset": Construct.objects.all(), 
		'template_name': 'construct_detail.html'
		,}, name="construct-detail"),
	url(r'^new/$', create_construct, {
		'model': Construct, 
		'template_name': 'construct_form.html', 
		'login_required':True 
		}, name="construct-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_construct, {
		'model': Construct, 
		'template_name': 'construct_form.html',
		'login_required':True 
		,}, name="construct-edit"),
	url(r'^(?P<object_id>[\d]+)/update$', change_construct, {
		'model': Construct, 
		'template_name': 'construct_form.html',
		'login_required':True 
		,}),		
	url(r'^(?P<object_id>[\d]+)/delete$', delete_construct, {
		'model': Construct, 
		'login_required':True,
		'template_name': 'confirm_delete.html',
		'post_delete_redirect': '/experimentdb/construct'
		,}, name="construct-delete"),
)
