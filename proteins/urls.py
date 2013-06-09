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

from django.conf.urls.defaults import *


urlpatterns = patterns('',			
	url(r'^(?P<protein_id>[\d]+)/$', 'proteins.views.protein_isoform_detail', name='protein-isoform-detail'),
	url(r'^(?P<protein>[-\w\d]+)/$', 'proteins.views.detail', name='protein-name-slug'))
