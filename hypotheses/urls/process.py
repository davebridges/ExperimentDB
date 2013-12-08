'''This is the urlconf for process objects.'''

from django.conf.urls import *

from hypotheses import views

urlpatterns = patterns('',
	url(r'^new/$', views.ProcessCreate.as_view(), name="process-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.ProcessDetail.as_view(), name="process-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.ProcessUpdate.as_view(), name="process-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.ProcessDelete.as_view(), name="process-delete"),
    url(r'^$', views.ProcessList.as_view(), name="process-list"),
)
