'''This is the urlconf for hypotheses.'''

from django.conf.urls.defaults import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.AntibodyCreate.as_view(), name="antibody-new"),
        url(r'^(?P<pk>[\dw-]+)/$', views.AntibodyDetail.as_view(), name="antibody-detail"),
	url(r'^(?P<pk>[\dw-]+)/edit$', views.AntibodyUpdate.as_view(), name="antibody-edit"),
	url(r'^(?P<pk>[\dw-]+)/delete$', views.AntibodyDelete.as_view(), name="antibody-delete"),
    url(r'^$', views.AntibodyList.as_view(), name="antibody-list"),
)

