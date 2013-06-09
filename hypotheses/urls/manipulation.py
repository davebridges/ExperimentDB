'''This is the urlconf for manipulation objects.'''

from django.conf.urls.defaults import *

from hypotheses import views

urlpatterns = patterns('',
	url(r'^new/$', views.ManipulationCreate.as_view(), name="manipulation-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.ManipulationDetail.as_view(), name="manipulation-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.ManipulationUpdate.as_view(), name="manipulation-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.ManipulationDelete.as_view(), name="manipulation-delete"),
    url(r'^$', views.ManipulationList.as_view(), name="manipulation-list"),
)