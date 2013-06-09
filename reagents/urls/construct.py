'''This is the urlconf for constructs.'''

from django.conf.urls.defaults import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.ConstructCreate.as_view(), name="construct-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.ConstructDetail.as_view(), name="construct-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.ConstructUpdate.as_view(), name="construct-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.ConstructDelete.as_view(), name="construct-delete"),
    url(r'^$', views.ConstructList.as_view(), name="construct-list"),
)

