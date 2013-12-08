"""
This package defines url redirections for the proteins app.

This app takes a url request in the form of /protein/something and redirects to the following views:
* protein-list
* protein-detail
* protein-new
* protein-edit
* protein-delete
* protein-family-list
* protein-family-detail
* protein-family-new
* protein-detail-new
* protein-detail-edit
* protein-detail-delete
* protein-isoform-detail
* protein-name-slug
"""

from django.conf.urls import *

from proteins import views

urlpatterns = patterns('',			
	url(r'^protein-detail/(?P<protein_id>[\d]+)/$', 'proteins.views.protein_isoform_detail', name='protein-isoform-detail'),
	url(r'^pritein-detail/(?P<protein>[-\w\d]+)/$', 'proteins.views.detail', name='protein-name-slug'),
	url(r'^/new/$', views.ProteinCreate.as_view(), name="protein-new"),
        url(r'^(?P<pk>\d+)/?$', views.ProteinDetail.as_view(), name='protein-detail'),        
	url(r'^(?P<pk>\d+)/edit/?$', views.ProteinUpdate.as_view(), name="protein-edit"),
	url(r'^(?P<pk>\d+)/delete/?$', views.ProteinDelete.as_view(), name="protein-delete"),
	url(r'^protein-family/new/$', views.ProteinFamilyCreate.as_view(), name="protein-family-new"),
        url(r'^protein-family/(?P<pk>\d+)/$', views.ProteinFamilyDetail.as_view(), name="protein-family-detail"),
	url(r'^protein-family/(?P<pk>\d+)/edit$', views.ProteinFamilyUpdate.as_view(), name="protein-family-edit"),
	url(r'^protein-family/(?P<pk>\d+)/delete$', views.ProteinFamilyDelete.as_view(), name="protein-family-delete"),
        url(r'^protein-family/$', views.ProteinFamilyList.as_view(), name="protein-family-list"),
        url(r'^protein-detail/new/?$', views.ProteinDetailCreate.as_view(), name="protein-detail-new"),
        url(r'^/?$', views.ProteinList.as_view(), name="protein-list")
)
