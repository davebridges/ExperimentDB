from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from experimentdb.reagents.models import Construct


construct_info = {
	"queryset": Construct.objects.all(),
	'template_name': 'construct_list.html',
}

construct_detail_info = {
	"queryset": Construct.objects.all(),
	'template_name': 'construct_detail.html',
}


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
	(r'^constructs?/$', 'django.views.generic.list_detail.object_list', construct_info),
	(r'^constructs?/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', construct_detail_info),
)
