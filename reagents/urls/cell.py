'''This is the urlconf for cell lines.'''

from django.conf.urls import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.CellCreate.as_view(), name="cell-new"),
        url(r'^(?P<pk>[\dw-]+)/$', views.CellDetail.as_view(), name="cell-detail"),
	url(r'^(?P<pk>[\dw-]+)/edit$', views.CellUpdate.as_view(), name="cell-edit"),
	url(r'^(?P<pk>[\dw-]+)/delete$', views.CellDelete.as_view(), name="cell-delete"),
    url(r'^$', views.CellList.as_view(), name="cell-list"),
)

