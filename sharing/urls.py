'''This is the urlconf for construct-shipment urls.'''

from django.conf.urls.defaults import *

from sharing import views

urlpatterns = patterns('',
	url(r'^new/$', views.ConstructShipmentCreate.as_view(), name="construct-shipment-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.ConstructShipmentDetail.as_view(), name="construct-shipment-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.ConstructShipmentUpdate.as_view(), name="construct-shipment-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.ConstructShipmentDelete.as_view(), name="construct-shipment-delete"),
    url(r'^$', views.ConstructShipmentList.as_view(), name="construct-shipment-list"),
)

