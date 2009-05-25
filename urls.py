from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from experimentdb.reagents.models import Construct, Antibody, Primer

urlpatterns = patterns('',
	(r'^admin/(.*)', admin.site.root),
	(r'^accounts/login/', 'django.contrib.auth.views.login'),
	(r'^experiment/(?P<experimentID>[-\w]+)/$', 'experimentdb.data.views.experiment'),
	(r'^experiments?/$', 'experimentdb.data.views.index'),
	(r'^search/$', 'experimentdb.views.search'),
	(r'^projects?/(?P<project>[-\w]+)/$', 'experimentdb.projects.views.detail'),		
	(r'^projects?/$', 'experimentdb.projects.views.index'),
	(r'^subprojects?/(?P<subproject>[-\w]+)/$', 'experimentdb.projects.views.subproject_detail'),
	(r'^proteins?/(?P<protein>[-\w\d]+)/$', 'experimentdb.proteins.views.detail'),		
	(r'^proteins?/$', 'experimentdb.proteins.views.index'),
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
	)
