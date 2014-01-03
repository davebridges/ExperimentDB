'''This is the urlconf for fly strains.'''

from django.conf.urls import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.FlyStrainCreate.as_view(), name="fly-strain-new"),
        url(r'^(?P<pk>[\dw-]+)/$', views.FlyStrainDetail.as_view(), name="fly-strain-detail"),
	url(r'^(?P<pk>[\dw-]+)/edit$', views.FlyStrainUpdate.as_view(), name="fly-strain-edit"),
	url(r'^(?P<pk>[\dw-]+)/delete$', views.FlyStrainDelete.as_view(), name="fly-strain-delete"),
        url(r'^$', views.FlyStrainList.as_view(), name="fly-strain-list"),
)

