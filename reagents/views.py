from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse

from experimentdb.reagents.models import Construct, Antibody, Chemical, Cell, Primer, Strain

@login_required
def index(request):
	constructs = Construct.objects.all()
	antibodies = Antibody.objects.all()
	chemicals = Chemical.objects.all()
	cells = Cell.objects.all()
	primers = Primer.objects.all()
	strains = Strain.objects.all()
	return render_to_response('reagent_list.html', {'constructs':constructs, 'antibodies':antibodies, 'proteins':proteins, 'chemicals': chemicals, 'cells':cells, 'primers':primers, 'strains':strains },context_instance=RequestContext(request)) 

	
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
