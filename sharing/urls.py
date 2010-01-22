from django.conf.urls.defaults import *

from experimentdb.sharing.models import ConstructShipment

urlpatterns = patterns('',
	(r'^new/$', 'django.views.generic.create_update.create_object', {
		'model': ConstructShipment, 
		'template_name': 'shipment_form.html', 
		'login_required':True ,
		}),
	(r'^(?P<object_id>[\d]+)/edit/$', 'django.views.generic.create_update.update_object', {
		'model': ConstructShipment, 
		'template_name': 'shipment.html', 
		'login_required':True ,
		}),
	(r'^$', 'django.views.generic.list_detail.object_list', {
		"queryset": ConstructShipment.objects.all(), 
		'template_name': 'shipment_list.html',
		}),
	(r'^mutagenesis/(?P<object_id>[\d]+)/$', 'django.views.generic.list_detail.object_detail', {
		"queryset": ConstructShipment.objects.all(), 
		'template_name': 'shipment_detail.html'
		,}),
)
