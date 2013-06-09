'''This is the urlconf for cell lines.'''

from django.conf.urls.defaults import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.CellCreate.as_view(), name="cell-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.CellDetail.as_view(), name="cell-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.CellUpdate.as_view(), name="cell-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.CellDelete.as_view(), name="cell-delete"),
    url(r'^$', views.CellList.as_view(), name="cell-list"),
)

