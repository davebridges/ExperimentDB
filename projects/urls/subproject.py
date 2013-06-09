from django.conf.urls.defaults import *

from projects import views

urlpatterns = patterns('',
	url(r'^new/$', views.SubProjectCreate.as_view(), name="subproject-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.SubProjectDetail.as_view(), name="subproject-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.SubProjectUpdate.as_view(), name="subproject-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.SubProjectDelete.as_view(), name="subproject-delete"),
    url(r'^$', views.SubProjectList.as_view(), name="subproject-list"),
)

