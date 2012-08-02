"""This package defines url routing for :class:`~reagents.models.License` objects.

"""

from django.conf.urls.defaults import *

from reagents import views

urlpatterns = patterns('',
	url(r'^(?P<pk>[\d]+)/?$', views.LicenseDetail.as_view(), name="license-detail"),
    url(r'^new/?$', views.LicenseCreate.as_view(), name="license-new"),
    url(r'^(?P<pk>[\d]+)/edit/?$', views.LicenseUpdate.as_view(), name="license-edit")
)
