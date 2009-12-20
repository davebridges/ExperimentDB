from django.conf.urls.defaults import *

from experimentdb.cloning.models import Cloning, Mutagenesis

urlpatterns = patterns('',
	(r'^plasmid/new/$', 'django.views.generic.create_update.create_object', {
		'model': Cloning, 
		'template_name': 'cloning_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/cloning/plasmid"
		}),
	(r'^mutagenesis/new/$', 'django.views.generic.create_update.create_object', {
		'model': Mutagenesis, 
		'template_name': 'mutagenesis_form.html', 
		'login_required':True ,
		'post_save_redirect':"/experimentdb/cloning/mutagenesis"
		}),
	(r'^mutagenesis/$', 'django.views.generic.list_detail.object_list', {
		"queryset": Mutagenesis.objects.all(), 
		'template_name': 'mutagenesis_list.html',
		}),
	(r'^mutagenesis/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Mutagenesis.objects.all(), 
		'template_name': 'mutagenesis_detail.html'
		,}),
)
