'''This is the urlconf for hypotheses.'''

from django.conf.urls.defaults import *

from hypotheses import views

urlpatterns = patterns('',
	url(r'^new/$', views.HypothesisCreate.as_view(), name="hypothesis-new"),
        url(r'^(?P<pk>[\d]+)/$', views.HypothesisDetail.as_view(), name="hypothesis-detail"),
	url(r'^(?P<pk>[\d]+)/edit$', views.HypothesisUpdate.as_view(), name="hypothesis-edit"),
	url(r'^(?P<pk>[\d]+)/delete$', views.HypothesisDelete.as_view(), name="hypothesis-delete"),
        url(r'^$', views.HypothesisList.as_view(), name="hypothesis-list"),
)

