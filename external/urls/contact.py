'''This is the urlconf for contact urls.'''

from django.conf.urls import *

from external import views

urlpatterns = patterns('',
	url(r'^new/$', views.ContactCreate.as_view(), name="contact-new"),
    url(r'^(?P<slug>[\w-]+)/$', views.ContactDetail.as_view(), name="contact-detail"),
	url(r'^(?P<slug>[\w-]+)/edit$', views.ContactUpdate.as_view(), name="contact-edit"),
	url(r'^(?P<slug>[\w-]+)/delete$', views.ContactDelete.as_view(), name="contact-delete"),
    url(r'^$', views.ContactList.as_view(), name="contact-list"),
)
