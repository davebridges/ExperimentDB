'''This is the urlconf for licences.'''

from django.conf.urls.defaults import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.LicenseCreate.as_view(), name="license-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.LicenseDetail.as_view(), name="license-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.LicenseUpdate.as_view(), name="license-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.LicenseDelete.as_view(), name="license-delete"),
    url(r'^$', views.LicenseList.as_view(), name="license-list"),
)

