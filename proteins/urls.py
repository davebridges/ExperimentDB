from django.conf.urls.defaults import *

from experimentdb.proteins.forms import ProteinForm
from experimentdb.proteins.models import ProteinFamily, ProteinDetail

urlpatterns = patterns('',
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'form_class': ProteinForm, 
		'template_name': 'protein_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/protein"
		}),
	(r'^family/$', 'django.views.generic.list_detail.object_list', {
		"queryset": ProteinFamily.objects.all(), 
		'template_name': 'protein_family_list.html',
		}),
	(r'^family/new/$', 'django.views.generic.create_update.create_object', {
		'model': ProteinFamily, 
		'template_name': 'protein_family_form.html', 
		'login_required':True ,
		'post_save_redirect': "/experimentdb/protein/family"
		}),	
	(r'^family/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": ProteinFamily.objects.all(), 
		'template_name': 'protein_family_detail.html'
		,}),
	(r'^$', 'experimentdb.proteins.views.index'),
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': ProteinDetail, 
		'template_name': 'proteindetail_form.html', 
		'login_required':True
	}),
	(r'^(?P<protein_id>[\d]+)/$', 'experimentdb.proteins.views.protein_isoform_detail'),
	(r'^(?P<protein>[-\w\d]+)/$', 'experimentdb.proteins.views.detail'),	
)
