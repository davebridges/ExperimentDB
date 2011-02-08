from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.hypotheses.models import Manipulation

@login_required
def manipulation_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def manipulation_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_manipulation')
def create_manipulation(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_manipulation')
def change_manipulation(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_manipulation')
def delete_manipulation(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', manipulation_list, {
		"queryset": Manipulation.objects.all(), 
		'template_name': 'manipulation_list.html',
		}, name="manipulation-list"),
	url(r'^(?P<object_id>[\d]+)/$', manipulation_detail, {
		"queryset": Manipulation.objects.all(), 
		'template_name': 'manipulation_detail.html'
		,}, name="manipulation-detail"),
	url(r'^new/$', create_manipulation, {
		'model': Manipulation, 
		'template_name': 'manipulation_form.html', 
		'login_required':True 
		}, name="manipulation-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_manipulation, {
		'model': Manipulation, 
		'template_name': 'manipulation_form.html',
		'login_required':True 
		,}, name="manipulation-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_manipulation, {
		'model': Manipulation, 
		'login_required':True,
		'template_name': 'confirm_delete.html',
		'post_delete_redirect': '/experimentdb/manipulation'
		,}, name="manipulation-delete"),
)
