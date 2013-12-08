'''This is the urlconf for strains.'''

from django.conf.urls import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.StrainCreate.as_view(), name="strain-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.StrainDetail.as_view(), name="strain-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.StrainUpdate.as_view(), name="strain-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.StrainDelete.as_view(), name="strain-delete"),
    url(r'^$', views.StrainList.as_view(), name="strain-list"),
)

