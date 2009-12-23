from django.conf.urls.defaults import *

from experimentdb.reagents.models import Cell

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', {
		"queryset": Cell.objects.all(), 
		'template_name': 'cell_list.html',
		}),
	(r'^(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Cell.objects.all(), 
		'template_name': 'cell_detail.html'
		,}),
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': Cell, 
		'template_name': 'cell_form.html', 
		'login_required':True 
		}),
	(r'^(?P<object_id>[\d]+)/edit$', 'django.views.generic.create_update.update_object', {
		'model': Cell, 
		'template_name': 'cell_form.html',
		'login_required':True 
		,}),
	(r'^(?P<object_id>[\d]+)/delete$', 'django.views.generic.create_update.delete_object', {
		'model': Cell, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/cell'
		,}),
)
