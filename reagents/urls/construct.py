'''This is the urlconf for constructs.'''

from django.conf.urls import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.ConstructCreate.as_view(), name="construct-new"),
        url(r'^(?P<pk>[\d-]+)/$', views.ConstructDetail.as_view(), name="construct-detail"),
	url(r'^(?P<pk>[\d-]+)/edit$', views.ConstructUpdate.as_view(), name="construct-edit"),
	url(r'^(?P<pk>[\d-]+)/delete$', views.ConstructDelete.as_view(), name="construct-delete"),
        url(r'^$', views.ConstructList.as_view(), name="construct-list"),
)

