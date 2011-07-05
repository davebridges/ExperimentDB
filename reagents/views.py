"""This package contains views for the reagents app."""

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView

from experimentdb.reagents.models import Construct, Antibody, Chemical, Cell, Primer, Strain, License

@login_required
def index(request):
	constructs = Construct.objects.all()
	antibodies = Antibody.objects.all()
	chemicals = Chemical.objects.all()
	cells = Cell.objects.all()
	primers = Primer.objects.all()
	strains = Strain.objects.all()
	return render_to_response('reagent_list.html', {'constructs':constructs, 'antibodies':antibodies, 'chemicals': chemicals, 'cells':cells, 'primers':primers, 'strains':strains },context_instance=RequestContext(request)) 

	
def antibody_lookup(request):
	"""A json lookup view for antibodies.
	
	This view takes a get query item and returns a json dictionary of antibody objects matching that name"""
	results = []
	if request.method == "GET":
		if request.GET.has_key(u'query'):
			value = request.GET[u'query']
			# Ignore queries shorter than length 3
			if len(value) > 2:
				model_results = Antibody.objects.filter(antibody__icontains=value)
				results = [ x.antibody for x in model_results ]
	json = simplejson.dumps(results)
	return HttpResponse(json, mimetype='application/json')
    
class LicenseDetail(DetailView):
    """This view displays specific details about a :class:`~experimentdb.models.License` object as the license-detail.
	
    It takes a request in the form **/license/(id)**, or **/mta/(id)** and renders the detail page for that license.  
    This page is restricted to logged-in users.
    """
    
    model = License
    template_name = 'license_detail.html'
    context_object_name = 'license'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """This decorator sets this view to have login restricted permissions."""
        return super(LicenseDetail, self).dispatch(*args, **kwargs)

class LicenseCreate(CreateView):
    """This view generates a page to create a new :class:`~experimentdb.models.License` object.
    
    It takes a url in the form of **/license/new** and renders the form for a new license."""
    
    model = License
    template_name = 'license_form.html'
    context_object_name = 'license'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """This decorator sets this view to have restricted permissions."""
        return super(LicenseCreate, self).dispatch(*args, **kwargs)

class LicenseUpdate(UpdateView):
    """This view generates a page to create a new :class:`~experimentdb.models.License` object.
    
    It takes a url in the form of **/license/#/edit** and renders the form for altering a license."""
    
    model = License
    template_name = 'license_form.html'
    context_object_name = 'license'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """This decorator sets this view to have restricted permissions."""
        return super(LicenseUpdate, self).dispatch(*args, **kwargs)         
