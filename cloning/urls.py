"""This package defines the url configuration for the cloning app.

All views in this app start from a request /cloning/cloning or /cloning/mutagenesis.
There are simple new, edit, delete, detail and list views for each of cloning and mutagenesis.
"""

'''This is the urlconf for protocol urls.'''

from django.conf.urls.defaults import *

from cloning import views

urlpatterns = patterns('',
	url(r'^cloning/new/$', views.CloningCreate.as_view(), name="cloning-new"),
    url(r'^cloning/(?P<pk>\d+)/$', views.CloningDetail.as_view(), name="cloning-detail"),
	url(r'^cloning/(?P<pk>\d+)/edit$', views.CloningUpdate.as_view(), name="cloning-edit"),
	url(r'^cloning/(?P<pk>\d+)/delete$', views.CloningDelete.as_view(), name="cloning-delete"),
    url(r'^cloning/$', views.CloningList.as_view(), name="cloning-list"),
	url(r'^mutagenesis/new/$', views.MutagenesisCreate.as_view(), name="mutagenesis-new"),
    url(r'^mutagenesis/(?P<pk>\d+)/$', views.MutagenesisDetail.as_view(), name="mutagenesis-detail"),
	url(r'^mutagenesis/(?P<pk>\d+)/edit$', views.MutagenesisUpdate.as_view(), name="mutagenesis-edit"),
	url(r'^mutagenesis/(?P<pk>\d+)/delete$', views.MutagenesisDelete.as_view(), name="mutagenesis-delete"),
    url(r'^mutagenesis/$', views.MutagenesisList.as_view(), name="mutagenesis-list"),    
)

