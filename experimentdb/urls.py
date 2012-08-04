from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from datasets.models import SGD_GeneNames, SGD_phenotypes, PI35P2_Binding_Screen_SP

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^accounts/login/', 'django.contrib.auth.views.login'),
	(r'^comments?/', include('django.contrib.comments.urls')),
	#(r'^search/$', 'views.search'),
	(r'^ajax_select/', include('ajax_select.urls')),
	(r'^add/protein_family/?$', 'proteins.views.newProteinFamily'),

	(r'^experiments?/', include('data.urls.experiment')),
	(r'^exps?/', include('data.urls.experiment')),

	url(r'^projects?/', include('projects.urls.project')),
	url(r'^subprojects?/', include('projects.urls.subproject')),

	url(r'^hypotheses/', include('hypotheses.urls.hypothesis')),
	url(r'^process/', include('hypotheses.urls.process')),
	url(r'^manipulation/', include('hypotheses.urls.manipulation')),    

	(r'^proteins?/', include('proteins.urls')),

	url(r'^reagents?/$', 'reagents.views.index', name="reagent-list"),

	url(r'^protocols?/', include('data.urls.protocol')),
	url(r'^protocols?/$', 'data.views.protocol_list'),
	url(r'^protocols?/(?P<protocol_slug>[-\w\d]+)/$', 'data.views.protocol_detail'),
	url(r'^sgd/(?P<gene>[-\w\d]+)/$', 'datasets.views.sgd_gene_detail', name="sgd-gene-detail"),

	url(r'^constructs?/', include('reagents.urls.construct')),
	url(r'^vectors?/', include('reagents.urls.construct')),
	url(r'^plasmids?/', include('reagents.urls.construct')),
	url(r'^recombinant-?dna/', include('reagents.urls.construct')),

	url(r'^antibodys?/', include('reagents.urls.antibody')),
	url(r'^antibodies?/', include('reagents.urls.antibody')),

	url(r'^primers?/', include('reagents.urls.primer')),

	url(r'^cells?/', include('reagents.urls.cell')),
	url(r'^cell-?lines?/', include('reagents.urls.cell')),
	url(r'^cultured-cell-?lines?/', include('reagents.urls.cell')),

	url(r'^chemicals?/', include('reagents.urls.chemical')),
	url(r'^drugs?/', include('reagents.urls.chemical')),
	url(r'^pharmaceuticals?/', include('reagents.urls.chemical')),
	url(r'^biopharmaceuticals?/', include('reagents.urls.chemical')),
	
	url(r'^strains?/', include('reagents.urls.strain')),
	url(r'^yeast_?strains?/', include('reagents.urls.strain')),
	url(r'^yeasts?/', include('reagents.urls.strain')),
    
    url(r'^licenses?/', include('reagents.urls.license')),
    url(r'^mtas?/', include('reagents.urls.license')),
	
	(r'^clones?/', include('cloning.urls')),
	(r'^clonings?/', include('cloning.urls')),
	
	(r'^shipments?/', include('sharing.urls')),
	(r'^sharings?/', include('sharing.urls')),
	(r'^sent_items?/', include('sharing.urls')),
	(r'^shipped_items?/', include('sharing.urls')),
	(r'^shipped?/', include('sharing.urls')),

        (r'^vendors?/', include('external.urls.vendor')),
        (r'^company/', include('external.urls.vendor')),
        (r'^companies/', include('external.urls.vendor')),
        (r'^contacts?/', include('external.urls.contact')),
        (r'^references?/', include('external.urls.reference')),

	)
