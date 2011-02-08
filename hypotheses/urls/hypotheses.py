from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.hypotheses.models import Hypothesis

@login_required
def hypothesis_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def hypothesis_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_hypothesis')
def create_hypothesis(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_hypothesis')
def change_hypothesis(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_hypothesis')
def delete_hypothesis(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', hypothesis_list, {
		"queryset": Hypothesis.objects.all(), 
		'template_name': 'hypothesis_list.html',
		}, name="hypothesis-list"),
	url(r'^(?P<object_id>[\d]+)/$', hypothesis_detail, {
		"queryset": Hypothesis.objects.all(), 
		'template_name': 'hypothesis_detail.html'
		,}, name="hypothesis-detail"),
	url(r'^new/$', create_hypothesis, {
		'model': Hypothesis, 
		'template_name': 'hypothesis_form.html', 
		'login_required':True 
		}, name="hypothesis-new"),
	url(r'^(?P<object_id>[\d]+)/edit$', change_hypothesis, {
		'model': Hypothesis, 
		'template_name': 'hypothesis_form.html',
		'login_required':True 
		,}, name="hypothesis-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_hypothesis, {
		'model': Hypothesis, 
		'login_required':True,
		'template_name': 'confirm_delete.html',
		'post_delete_redirect': '/experimentdb/hypothesis'
		,}, name="hypothesis-delete"),
)
