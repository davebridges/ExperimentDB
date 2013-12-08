'''This is the urlconf for purified proteins.'''

from django.conf.urls import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.PurifiedProteinCreate.as_view(), name="purified-protein-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.PurifiedProteinDetail.as_view(), name="purified-protein-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.PurifiedProteinUpdate.as_view(), name="purified-protein-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.PurifiedProteinDelete.as_view(), name="purified-protein-delete"),
    url(r'^$', views.PurifiedProteinList.as_view(), name="purified-protein-list"),
)

