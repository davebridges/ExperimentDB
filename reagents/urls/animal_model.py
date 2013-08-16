'''This is the urlconf for animal models, served from /animal_models.'''

from django.conf.urls.defaults import *

from reagents import views

urlpatterns = patterns('',
	url(r'^new/$', views.AnimalStrainCreate.as_view(), name="animal-new"),
        url(r'^(?P<pk>[\dw-]+)/$', views.AnimalStrainDetail.as_view(), name="animal-detail"),
	url(r'^(?P<pk>[\dw-]+)/edit$', views.AnimalStrainUpdate.as_view(), name="animal-edit"),
	url(r'^(?P<pk>[\dw-]+)/delete$', views.AnimalStrainDelete.as_view(), name="animal-delete"),
        url(r'^$', views.AnimalStrainList.as_view(), name="animal-list"),
)

