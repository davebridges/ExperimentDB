from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from datasets.models import SGD_GeneNames, SGD_phenotypes
from experimentdb import views

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^accounts/login/', 'django.contrib.auth.views.login'),
	(r'^comments?/', include('django.contrib.comments.urls')),
	url(r'^search/$', views.search, name='search'),
	(r'^ajax_select/', include('ajax_select.urls')),
	(r'^add/protein_family/?$', 'proteins.views.newProteinFamily'),

	(r'^experiments?/', include('data.urls.experiment')),

	(r'^projects?/', include('projects.urls.project')),
	(r'^subprojects?/', include('projects.urls.subproject')),

	(r'^hypotheses/', include('hypotheses.urls.hypothesis')),
	(r'^process/', include('hypotheses.urls.process')),
	(r'^manipulation/', include('hypotheses.urls.manipulation')),    

	(r'^proteins?/', include('proteins.urls')),

	url(r'^reagents?/$', 'reagents.views.index', name="reagent-list"),

	(r'^protocols?/', include('data.urls.protocol')),
	url(r'^sgd/(?P<gene>[-\w\d]+)/$', 'datasets.views.sgd_gene_detail', name="sgd-gene-detail"),

	(r'^constructs?/', include('reagents.urls.construct')),

	(r'^antibodies/', include('reagents.urls.antibody')),

	(r'^primers?/', include('reagents.urls.primer')),

	(r'^cell-lines?/', include('reagents.urls.cell')),

	(r'^chemicals?/', include('reagents.urls.chemical')),
	
	(r'^yeast_strains?/', include('reagents.urls.strain')),
    
    (r'^licenses?/', include('reagents.urls.license')),
	
	(r'^clonings?/', include('cloning.urls')),
	
	(r'^shipments?/', include('sharing.urls')),

    (r'^vendors?/', include('external.urls.vendor')),
    (r'^contacts?/', include('external.urls.contact')),
    (r'^references?/', include('external.urls.reference')),
    
    url(r'^$', views.index, name='home'),

	)
