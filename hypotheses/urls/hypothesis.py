'''This is the urlconf for hypotheses.'''

from django.conf.urls.defaults import *

from hypotheses import views

urlpatterns = patterns('',
	url(r'^new/$', views.HypothesisCreate.as_view(), name="hypothesis-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.HypothesisDetail.as_view(), name="hypothesis-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.HypothesisUpdate.as_view(), name="hypothesis-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.HypothesisDelete.as_view(), name="hypothesis-delete"),
    url(r'^$', views.HypothesisList.as_view(), name="hypothesis-list"),
)

