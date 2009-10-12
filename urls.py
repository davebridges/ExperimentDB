from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from experimentdb.proteins.models import Protein, ProteinFamily, ProteinDetail
from experimentdb.reagents.models import Construct, Antibody, Primer, Purified_Protein, Chemical, Cell
from experimentdb.datasets.models import SGD_GeneNames, SGD_phenotypes, PI35P2_Binding_Screen_SP

from experimentdb.proteins.forms import ProteinForm
from experimentdb.data.forms import ExperimentForm


urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^accounts/login/', 'django.contrib.auth.views.login'),
	(r'^experiment?/new/$', 'django.views.generic.create_update.create_object', {
		'form_class': ExperimentForm, 
		'template_name': 'experiment_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/experiments"
		}),
	(r'^experiment/(?P<experimentID>[-\w]+)/$', 'experimentdb.data.views.experiment'),
	(r'^experiments?/$', 'experimentdb.data.views.index'),
	(r'^search/$', 'experimentdb.views.search'),
	(r'^projects?/(?P<project>[-\w]+)/$', 'experimentdb.projects.views.detail'),		
	(r'^projects?/$', 'experimentdb.projects.views.index'),
	(r'^subprojects?/(?P<subproject>[-\w]+)/$', 'experimentdb.projects.views.subproject_detail'),
	(r'^proteins?/new/$', 'django.views.generic.create_update.create_object', {
		'form_class': ProteinForm, 
		'template_name': 'protein_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/protein"
		}),
	(r'^proteins?/family/$', 'django.views.generic.list_detail.object_list', {
		"queryset": ProteinFamily.objects.all(), 
		'template_name': 'protein_family_list.html',
		}),
	(r'^proteins?/family/new/$', 'django.views.generic.create_update.create_object', {
		'model': ProteinFamily, 
		'template_name': 'protein_family_form.html', 
		'login_required':True ,
		'post_save_redirect': "/experimentdb/protein/family"
		}),	
	(r'^proteins?/family/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": ProteinFamily.objects.all(), 
		'template_name': 'protein_family_detail.html'
		,}),
	(r'^proteins?/$', 'experimentdb.proteins.views.index'),
	(r'^protein_isoform/new/$', 'django.views.generic.create_update.create_object', {
		'model': ProteinDetail, 
		'template_name': 'proteindetail_form.html', 
		'login_required':True
	}),
	(r'^protein_isoform/(?P<protein_id>[\d]+)/$', 'experimentdb.proteins.views.protein_isoform_detail'),
	(r'^proteins?/(?P<protein>[-\w\d]+)/$', 'experimentdb.proteins.views.detail'),	
	(r'^reagents?/$', 'experimentdb.reagents.views.index'),
	(r'^protocol?/$', 'experimentdb.data.views.protocol_list'),
	(r'^protocol?/(?P<protocol_slug>[-\w\d]+)/$', 'experimentdb.data.views.protocol_detail'),
	(r'^sgd/(?P<gene>[-\w\d]+)/$', 'experimentdb.datasets.views.sgd_gene_detail'),
	(r'^constructs?/$', 'django.views.generic.list_detail.object_list', {
		"queryset": Construct.objects.all(), 
		'template_name': 'construct_list.html',
		}),
	(r'^constructs?/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Construct.objects.all(), 
		'template_name': 'construct_detail.html'
		,}),
	(r'^construct/new/$', 'django.views.generic.create_update.create_object', {
		'model': Construct, 
		'template_name': 'construct_form.html', 
		'login_required':True 
		}),
	(r'^construct/(?P<object_id>[\d]+)/update/$', 'django.views.generic.create_update.update_object', {
		'model': Construct, 
		'template_name': 'construct_update.html', 
		'login_required':True 
		}),
	(r'^antibody/$', 'django.views.generic.list_detail.object_list', {
		"queryset": Antibody.objects.all(), 
		'template_name': 'antibody_list.html',
		}),
	(r'^antibody/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Antibody.objects.all(), 
		'template_name': 'antibody_detail.html'
		,}),
	(r'^antibody/new/$', 'django.views.generic.create_update.create_object', {
		'model': Antibody, 
		'template_name': 'antibody_form.html', 
		'login_required':True 
		}),
	(r'^primer/$', 'django.views.generic.list_detail.object_list', {
		"queryset": Primer.objects.all(), 
		'template_name': 'primer_list.html',
		}),
	(r'^primer/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Primer.objects.all(), 
		'template_name': 'primer_detail.html'
		,}),
	(r'^primer/new/$', 'django.views.generic.create_update.create_object', {
		'model': Primer, 
		'template_name': 'primer_form.html', 
		'login_required':True 
		}),
	(r'^cell/$', 'django.views.generic.list_detail.object_list', {
		"queryset": Cell.objects.all(), 
		'template_name': 'cell_list.html',
		}),
	(r'^cell/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Cell.objects.all(), 
		'template_name': 'cell_detail.html'
		,}),
	(r'^cell/new/$', 'django.views.generic.create_update.create_object', {
		'model': Cell, 
		'template_name': 'cell_form.html', 
		'login_required':True 
		}),	
	(r'^purified/$', 'django.views.generic.list_detail.object_list', {
		"queryset": Purified_Protein.objects.all(), 
		'template_name': 'purified_list.html',
		}),
	(r'^purified/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Primer.objects.all(), 
		'template_name': 'purified_detail.html'
		,}),
	(r'^purified/new/$', 'django.views.generic.create_update.create_object', {
		'model': Purified_Protein, 
		'template_name': 'purified_form.html', 
		'login_required':True 
		}),
	(r'^chemical/$', 'django.views.generic.list_detail.object_list', {
		"queryset": Chemical.objects.all(), 
		'template_name': 'chemical_list.html',
		}),
	(r'^chemical/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Chemical.objects.all(), 
		'template_name': 'chemical_detail.html'
		,}),
	(r'^chemical/new/$', 'django.views.generic.create_update.create_object', {
		'model': Chemical, 
		'template_name': 'chemical_form.html', 
		'login_required':True 
		}),
	(r'^pi35p2bp/$', 'django.views.generic.list_detail.object_list', {
		"queryset": PI35P2_Binding_Screen_SP.objects.all(),
		'template_name': 'gene_list.html',
		}),



	)
