'''This is the urlconf for vendor urls.'''

from django.conf.urls import *

from external import views

urlpatterns = patterns('',
	url(r'^new/$', views.VendorCreate.as_view(), name="vendor-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.VendorDetail.as_view(), name="vendor-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.VendorUpdate.as_view(), name="vendor-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.VendorDelete.as_view(), name="vendor-delete"),
    url(r'^$', views.VendorList.as_view(), name="vendor-list"),
)
