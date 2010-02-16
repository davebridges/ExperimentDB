from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
from django.contrib.auth.decorators import login_required, permission_required

from experimentdb.sharing.models import ConstructShipment

@login_required
def shipment_list(*args, **kwargs):
	return object_list(*args, **kwargs)

@login_required
def shipment_detail(*args, **kwargs):
	return object_detail(*args, **kwargs)

@permission_required('reagents.add_shipment')
def create_shipment(*args, **kwargs):
	return create_object(*args, **kwargs)

@permission_required('reagents.change_shipment')
def change_shipment(*args, **kwargs):
	return update_object(*args, **kwargs)

@permission_required('reagents.delete_shipment')
def delete_shipment(*args, **kwargs):
	return delete_object(*args, **kwargs)


urlpatterns = patterns('',
	url(r'^new/$', create_shipment, {
		'model': ConstructShipment, 
		'template_name': 'shipment_form.html', 
		'login_required':True ,
		}, name="shipment-new"),
	url(r'^(?P<object_id>[\d]+)/edit/$', change_shipment, {
		'model': ConstructShipment, 
		'template_name': 'shipment.html', 
		'login_required':True ,
		}, name="shipment-edit"),
	url(r'^$', shipment_list, {
		"queryset": ConstructShipment.objects.all(), 
		'template_name': 'shipment_list.html',
		}, name="shipment-list"),
	url(r'^(?P<object_id>[\d]+)/$', shipment_detail, {
		"queryset": ConstructShipment.objects.all(), 
		'template_name': 'shipment_detail.html'
		,}, name="shipment-detail"),
	url(r'^(?P<object_id>[\d]+)/delete$', delete_shipment, {
		'model': ConstructShipment, 
		'login_required':True,
		'post_delete_redirect': '/experimentdb/shipments'
		,}, name="shipment-delete"),
	)
