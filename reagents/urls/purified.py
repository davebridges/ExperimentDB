from django.conf.urls.defaults import *

from experimentdb.reagents.models import Purified_Protein

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', {
		"queryset": Purified_Protein.objects.all(), 
		'template_name': 'purified_list.html',
		}),
	(r'^(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": Purified_Protein.objects.all(), 
		'template_name': 'purified_detail.html'
		,}),
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': Purified_Protein, 
		'template_name': 'purified_form.html', 
		'login_required':True 
		}),
)
