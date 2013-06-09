'''This is the urlconf for protocol urls.'''

from django.conf.urls.defaults import *

from data import views

urlpatterns = patterns('',
	url(r'^new/$', views.ProtocolCreate.as_view(), name="protocol-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.ProtocolDetail.as_view(), name="protocol-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.ProtocolUpdate.as_view(), name="protocol-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.ProtocolDelete.as_view(), name="protocol-delete"),
    url(r'^$', views.ProtocolList.as_view(), name="protocol-list"),
)
