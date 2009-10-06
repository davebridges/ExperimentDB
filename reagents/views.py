from experimentdb.reagents.models import Construct, Antibody, Purified_Protein, Chemical, Cell, Primer
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	constructs = Construct.objects.all()
	antibodies = Antibody.objects.all()
	proteins = Purified_Protein.objects.all()
	chemicals = Chemical.objects.all()
	cells = Cell.objects.all()
	primers = Primer.objects.all()
	return render_to_response('reagent_list.html', {'constructs':constructs, 'antibodies':antibodies, 'proteins':proteins, 'chemicals': chemicals, 'cells':cells, 'primers':primers},context_instance=RequestContext(request)) 

	
	













