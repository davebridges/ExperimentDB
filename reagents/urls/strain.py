from django.conf.urls.defaults import *

from experimentdb.reagents.models import Strain

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', {
		"queryset": Strain.objects.all(), 
		'template_name': 'strain_list.html',
		}),
	(r'^(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Strain.objects.all(), 
		'template_name': 'strain_detail.html'
		,}),
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': Strain, 
		'template_name': 'strain_form.html', 
		'login_required':True 
		}),
	(r'^(?P<object_id>[\d]+)/edit$', 'django.views.generic.create_update.update_object', {
		'model': Strain,
		'template_name': 'strain_form.html',
		'login_required':True 
		,}),
	(r'^(?P<object_id>[\d]+)/update$', 'django.views.generic.create_update.update_object', {
		'model': Strain,
		'template_name': 'strain_form.html',
		'login_required':True 
		,}),
	(r'^(?P<object_id>[\d]+)/delete$', 'django.views.generic.create_update.delete_object', {
		'model': Strain,
		'template_name': 'strain_form.html',
		'login_required':True ,
		'post_delete_redirect': "/experimentdb/strain"
		,}),
)
