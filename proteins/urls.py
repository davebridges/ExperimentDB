from django.conf.urls.defaults import *

from experimentdb.proteins.forms import ProteinForm
from experimentdb.proteins.models import ProteinFamily, ProteinDetail

urlpatterns = patterns('',
	url(r'^new/$', 'django.views.generic.create_update.create_object', {
		'form_class': ProteinForm, 
		'template_name': 'protein_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/protein"
		}, name='protein-new'),
	url(r'^family/$', 'django.views.generic.list_detail.object_list', {
		"queryset": ProteinFamily.objects.all(), 
		'template_name': 'protein_family_list.html',
		}, name='protein-family-list'),
	url(r'^family/new/$', 'django.views.generic.create_update.create_object', {
		'model': ProteinFamily, 
		'template_name': 'protein_family_form.html', 
		'login_required':True ,
		'post_save_redirect': "/experimentdb/protein/family"
		}, name='protein-family-new'),	
	url(r'^family/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": ProteinFamily.objects.all(), 
		'template_name': 'protein_family_detail.html'
		,}, name='protein-family-detail'),
	url(r'^$', 'experimentdb.proteins.views.index', name='protein-new'),
	url(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': ProteinDetail, 
		'template_name': 'proteindetail_form.html', 
		'login_required':True
		}, name='protein-new'),
	url(r'^(?P<protein_id>[\d]+)/$', 'experimentdb.proteins.views.protein_isoform_detail', name='protein-isoform-detail'),
	url(r'^(?P<protein>[-\w\d]+)/$', 'experimentdb.proteins.views.detail', name='protein-detail'),	
)
