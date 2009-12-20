from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from experimentdb.datasets.models import SGD_GeneNames, SGD_phenotypes, PI35P2_Binding_Screen_SP

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^accounts/login/', 'django.contrib.auth.views.login'),
	(r'^comments?/', include('django.contrib.comments.urls')),
	(r'^search/$', 'experimentdb.views.search'),

	(r'^experiments?/', include('experimentdb.data.urls.experiment')),
	(r'^exps?/', include('experimentdb.data.urls.experiment')),

	(r'^projects?/', include('experimentdb.projects.urls.project')),
	(r'^subprojects?/', include('experimentdb.projects.urls.subproject')),

	(r'^proteins?/', include('experimentdb.proteins.urls')),

	(r'^reagents?/$', 'experimentdb.reagents.views.index'),

	(r'^protocol?/$', 'experimentdb.data.views.protocol_list'),
	(r'^protocol?/(?P<protocol_slug>[-\w\d]+)/$', 'experimentdb.data.views.protocol_detail'),
	(r'^sgd/(?P<gene>[-\w\d]+)/$', 'experimentdb.datasets.views.sgd_gene_detail'),

	(r'^constructs?/', include('experimentdb.reagents.urls.construct')),
	(r'^vectors?/', include('experimentdb.reagents.urls.construct')),
	(r'^plasmids?/', include('experimentdb.reagents.urls.construct')),
	(r'^recombinant-?dna?/', include('experimentdb.reagents.urls.construct')),

	(r'^antibodys?/', include('experimentdb.reagents.urls.antibody')),
	(r'^antibodies?/', include('experimentdb.reagents.urls.antibody')),

	(r'^primers?/', include('experimentdb.reagents.urls.primer')),

	(r'^cells?/', include('experimentdb.reagents.urls.cell')),
	(r'^cell-?lines?/', include('experimentdb.reagents.urls.cell')),
	(r'^cultured-cell-?lines?/', include('experimentdb.reagents.urls.cell')),

	(r'^purifieds?/', include('experimentdb.reagents.urls.purified')),
	(r'^purified-?proteins?/', include('experimentdb.reagents.urls.purified')),
	(r'^recombinant-?proteins?/', include('experimentdb.reagents.urls.purified')),

	(r'^chemicals?/', include('experimentdb.reagents.urls.purified')),
	(r'^drugs?/', include('experimentdb.reagents.urls.purified')),
	(r'^pharmaceuticals?/', include('experimentdb.reagents.urls.purified')),
	(r'^biopharmaceuticals?/', include('experimentdb.reagents.urls.purified')),
	
	(r'^strains?/', include('experimentdb.reagents.urls.strain')),
	(r'^yeast_?strains?/', include('experimentdb.reagents.urls.strain')),
	(r'^yeasts?/', include('experimentdb.reagents.urls.strain')),
	
	(r'^clones?/', include('experimentdb.cloning.urls')),
	(r'^clonings?/', include('experimentdb.cloning.urls')),

	(r'^pi35p2bp/$', 'django.views.generic.list_detail.object_list', {
		"queryset": PI35P2_Binding_Screen_SP.objects.all(),
		'template_name': 'gene_list.html',
		}),
	)
