"""This package defines the url redirections for the cloning app.

All views in this app start from a request of /experimentdb/cloning and direct to the following views:
* cloning-new
* mutagenesis-new
* mutagenesis-detail
* mutagenesis-edit
* mutagenesis-list

"""

from django.conf.urls.defaults import *

from experimentdb.cloning.models import Cloning, Mutagenesis

urlpatterns = patterns('',
	url(r'^plasmid/new/$', 'django.views.generic.create_update.create_object', {
		'model': Cloning, 
		'template_name': 'cloning_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/cloning/plasmid"
		}, name="cloning-new"),
	url(r'^mutagenesis/new/$', 'django.views.generic.create_update.create_object', {
		'model': Mutagenesis, 
		'template_name': 'mutagenesis_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/cloning/mutagenesis"
		}, name="mutagenesis-new"),
	url(r'^mutagenesis/(?P<object_id>[\d]+)/edit/$', 'django.views.generic.create_update.update_object', {
		'model': Mutagenesis, 
		'template_name': 'mutagenesis_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/cloning/mutagenesis"
		}, name="mutagenesis-edit"),
	url(r'^mutagenesis/$', 'django.views.generic.list_detail.object_list', {
		"queryset": Mutagenesis.objects.all(), 
		'template_name': 'mutagenesis_list.html',
		}, name="mutagenesis-list"),
	url(r'^mutagenesis/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Mutagenesis.objects.all(), 
		'template_name': 'mutagenesis_detail.html'
		,}, name="mutagenesis-detail"),
)
