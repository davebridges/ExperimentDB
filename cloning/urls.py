"""This package defines the url redirections for the cloning app.

All views in this app start from a request of /experimentdb/cloning and direct to the following views:
* cloning-new
* mutagenesis-new
* mutagenesis-detail
* mutagenesis-edit
* mutagenesis-list

"""

from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

from cloning.models import Cloning, Mutagenesis
from cloning import views

urlpatterns = patterns('',
	url(r'^plasmid/new/$', 'django.views.generic.create_update.create_object', {
		'model': Cloning, 
		'template_name': 'cloning_form.html', 
		'login_required':True 
		}, name="cloning-new"),
	url(r'^cloning/(?P<pk>\d+)/$', views.CloningDetailView.as_view(), name='cloning_detail'),	
	url(r'^mutagenesis/new/$', 'django.views.generic.create_update.create_object', {
		'model': Mutagenesis, 
		'template_name': 'mutagenesis_form.html', 
		'login_required':True
		}, name="mutagenesis-new"),
	url(r'^mutagenesis/(?P<object_id>[\d]+)/edit/$', 'django.views.generic.create_update.update_object', {
		'model': Mutagenesis, 
		'template_name': 'mutagenesis_form.html', 
		'login_required':True 
		}, name="mutagenesis-edit"),
	url(r'^mutagenesis/$', 'django.views.generic.list_detail.object_list', {
		"queryset": Mutagenesis.objects.all(), 
		'template_name': 'mutagenesis_list.html',
		}, name="mutagenesis-list"),
	url(r'^mutagenesis/(?P<pk>\d+)/$', views.MutagenesisDetailView.as_view(), name='mutagenesis_detail'),
)
