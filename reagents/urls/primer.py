'''This is the urlconf for hypotheses.'''

from django.conf.urls.defaults import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.PrimerCreate.as_view(), name="primer-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.PrimerDetail.as_view(), name="primer-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.PrimerUpdate.as_view(), name="primer-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.PrimerDelete.as_view(), name="primer-delete"),
    url(r'^$', views.PrimerList.as_view(), name="primer-list"),
)

