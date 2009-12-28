from django.conf.urls.defaults import *

from experimentdb.reagents.models import Primer

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', {
		"queryset": Primer.objects.all(), 
		'template_name': 'primer_list.html',
		}),
	(r'^(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Primer.objects.all(), 
		'template_name': 'primer_detail.html'
		,}),
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': Primer, 
		'template_name': 'primer_form.html', 
		'login_required':True ,
		}),
	(r'^(?P<object_id>[\d]+)/edit$', 'django.views.generic.create_update.update_object', {
		'model': Primer, 
		'template_name': 'primer_form.html',
		'login_required':True 
		,}),
	(r'^(?P<object_id>[\d]+)/delete$', 'django.views.generic.create_update.delete_object', {
		'model': Primer, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/primer'
		,}),
)
