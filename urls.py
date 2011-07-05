from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from experimentdb.datasets.models import SGD_GeneNames, SGD_phenotypes, PI35P2_Binding_Screen_SP

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^accounts/login/', 'django.contrib.auth.views.login'),
	(r'^comments?/', include('django.contrib.comments.urls')),
	(r'^search/$', 'experimentdb.views.search'),
	(r'^ajax_select/', include('ajax_select.urls')),
	(r'^add/protein_family/?$', 'experimentdb.proteins.views.newProteinFamily'),

	(r'^experiments?/', include('experimentdb.data.urls.experiment')),
	(r'^exps?/', include('experimentdb.data.urls.experiment')),

	url(r'^projects?/', include('experimentdb.projects.urls.project')),
	url(r'^subprojects?/', include('experimentdb.projects.urls.subproject')),

	url(r'^hypotheses/', include('experimentdb.hypotheses.urls.hypotheses')),
	url(r'^process/', include('experimentdb.hypotheses.urls.process')),
	url(r'^manipulation/', include('experimentdb.hypotheses.urls.manipulation')),    

	(r'^proteins?/', include('experimentdb.proteins.urls')),

	url(r'^reagents?/$', 'experimentdb.reagents.views.index', name="reagent-list"),

	url(r'^protocols?/', include('experimentdb.data.urls.protocol')),
	url(r'^protocols?/$', 'experimentdb.data.views.protocol_list'),
	url(r'^protocols?/(?P<protocol_slug>[-\w\d]+)/$', 'experimentdb.data.views.protocol_detail'),
	url(r'^sgd/(?P<gene>[-\w\d]+)/$', 'experimentdb.datasets.views.sgd_gene_detail', name="sgd-gene-detail"),

	url(r'^constructs?/', include('experimentdb.reagents.urls.construct')),
	url(r'^vectors?/', include('experimentdb.reagents.urls.construct')),
	url(r'^plasmids?/', include('experimentdb.reagents.urls.construct')),
	url(r'^recombinant-?dna/', include('experimentdb.reagents.urls.construct')),

	url(r'^antibodys?/', include('experimentdb.reagents.urls.antibody')),
	url(r'^antibodies?/', include('experimentdb.reagents.urls.antibody')),

	url(r'^primers?/', include('experimentdb.reagents.urls.primer')),

	url(r'^cells?/', include('experimentdb.reagents.urls.cell')),
	url(r'^cell-?lines?/', include('experimentdb.reagents.urls.cell')),
	url(r'^cultured-cell-?lines?/', include('experimentdb.reagents.urls.cell')),

	url(r'^chemicals?/', include('experimentdb.reagents.urls.chemical')),
	url(r'^drugs?/', include('experimentdb.reagents.urls.chemical')),
	url(r'^pharmaceuticals?/', include('experimentdb.reagents.urls.chemical')),
	url(r'^biopharmaceuticals?/', include('experimentdb.reagents.urls.chemical')),
	
	url(r'^strains?/', include('experimentdb.reagents.urls.strain')),
	url(r'^yeast_?strains?/', include('experimentdb.reagents.urls.strain')),
	url(r'^yeasts?/', include('experimentdb.reagents.urls.strain')),
    
    url(r'^licenses?/', include('experimentdb.reagents.urls.license')),
    url(r'^mtas?/', include('experimentdb.reagents.urls.license')),
	
	(r'^clones?/', include('experimentdb.cloning.urls')),
	(r'^clonings?/', include('experimentdb.cloning.urls')),
	
	(r'^shipments?/', include('experimentdb.sharing.urls')),
	(r'^sharings?/', include('experimentdb.sharing.urls')),
	(r'^sent_items?/', include('experimentdb.sharing.urls')),
	(r'^shipped_items?/', include('experimentdb.sharing.urls')),
	(r'^shipped?/', include('experimentdb.sharing.urls')),

        (r'^vendors?/', include('experimentdb.external.urls.vendor')),
        (r'^company/', include('experimentdb.external.urls.vendor')),
        (r'^companies/', include('experimentdb.external.urls.vendor')),
        (r'^contacts?/', include('experimentdb.external.urls.contact')),
        (r'^references?/', include('experimentdb.external.urls.reference')),
	

	(r'^pi35p2bp/$', 'django.views.generic.list_detail.object_list', {
		"queryset": PI35P2_Binding_Screen_SP.objects.all(),
		'template_name': 'gene_list.html',
		}),
	)
