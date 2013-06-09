'''This is the urlconf for chemicals.'''

from django.conf.urls.defaults import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.ChemicalCreate.as_view(), name="chemical-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.ChemicalDetail.as_view(), name="chemical-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.ChemicalUpdate.as_view(), name="chemical-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.ChemicalDelete.as_view(), name="chemical-delete"),
    url(r'^$', views.ChemicalList.as_view(), name="chemical-list"),
)

