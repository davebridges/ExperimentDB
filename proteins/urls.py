from django.conf.urls.defaults import *
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.list_detail import object_list, object_detail

from experimentdb.proteins.forms import ProteinForm
from experimentdb.proteins.models import ProteinFamily, ProteinDetail, Protein

@login_required
def restricted_object_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def restricted_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('proteins.add_protein')
def restricted_create_protein(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('proteins.change_protein')
def restricted_change_protein(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_protein')
def restricted_delete_protein(*args, **kwargs):
	return delete_object(*args, **kwargs)

urlpatterns = patterns('',
	url(r'^$', restricted_object_list, {
		"queryset": Protein.objects.all(), 
		'template_name': 'protein_list.html',
		'template_object_name':'protein',
		}, name='protein-list'),	
	url(r'(?P<object_id>[\d]+)/$', restricted_detail, {
		"queryset": Protein.objects.all(), 
		'template_name': 'protein_detail.html'
		,}, name='protein-detail'),
	url(r'^new/$', restricted_create_protein, {
		'form_class': ProteinForm, 
		'template_name': 'protein_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/protein"
		}, name='protein-new'),
	url(r'^(?P<object_id>[\d]+)/edit$', restricted_change_protein, {
		'model': Protein, 
		'template_name': 'protein_form.html',
		'login_required':True 
		,}, name="protein-edit"),
	url(r'^(?P<object_id>[\d]+)/delete$', restricted_delete_protein, {
		'model': Protein, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/protein'
		,}, name="protein-delete"),		
	url(r'^family/$', restricted_object_list, {
		"queryset": ProteinFamily.objects.all(), 
		'template_name': 'protein_family_list.html',
		}, name='protein-family-list'),
	url(r'^family/(?P<object_id>[\d]+)/$', restricted_detail, {
		"queryset": ProteinFamily.objects.all(), 
		'template_name': 'protein_family_detail.html'
		,}, name='protein-family-detail'),
	url(r'^family/new/$', restricted_create_protein, {
		'model': ProteinFamily, 
		'template_name': 'protein_family_form.html', 
		'login_required':True ,
		'post_save_redirect': "/experimentdb/protein/family"
		}, name='protein-family-new'),	
	url(r'^detail/new/$', restricted_create_protein, {
		'model': ProteinDetail, 
		'template_name': 'proteindetail_form.html', 
		'login_required':True
		}, name='protein-detail-new'),
	url(r'^detail/(?P<object_id>[\d]+)/edit$', restricted_change_protein, {
		'model': ProteinDetail, 
		'template_name': 'proteindetail_form.html',
		'login_required':True 
		,}, name="protein-detail-edit"),
	url(r'^detail/(?P<object_id>[\d]+)/delete$', restricted_delete_protein, {
		'model': ProteinDetail, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/protein'
		,}, name="protein-detail-delete"),			
	url(r'^(?P<protein_id>[\d]+)/$', 'experimentdb.proteins.views.protein_isoform_detail'),
	url(r'^(?P<protein>[-\w\d]+)/$', 'experimentdb.proteins.views.detail', name='protein-name-slug'),	
)
