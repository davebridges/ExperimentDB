'''This is the urlconf for reference urls.'''

from django.conf.urls.defaults import *

from external import views

urlpatterns = patterns('',
	url(r'^new/$', views.ReferenceCreate.as_view(), name="reference-new"),
    url(r'^(?P<slug>[-\w]+)/$', views.ReferenceDetail.as_view(), name="reference-details"),
	url(r'^(?P<slug>[-\w]+)/edit$', views.ReferenceUpdate.as_view(), name="reference-edit"),
	url(r'^(?P<slug>[-\w]+)/delete$', views.ReferenceDelete.as_view(), name="reference-delete"),
    url(r'^$', views.ReferenceList.as_view(), name="reference-list"),
)
