'''This is the urlconf for licences.'''

from django.conf.urls import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/?$', views.LicenseCreate.as_view(), name="license-new"),
    url(r'^(?P<pk>\d+)/?$', views.LicenseDetail.as_view(), name="license-detail"),
	url(r'^(?P<pk>\d+)/edit/?$', views.LicenseUpdate.as_view(), name="license-edit"),
	url(r'^(?P<pk>\d+)/delete/?$', views.LicenseDelete.as_view(), name="license-delete"),
    url(r'^/?$', views.LicenseList.as_view(), name="license-list"),
)

