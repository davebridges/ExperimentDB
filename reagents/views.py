from experimentdb.reagents.models import Construct, Antibody, Purified_Protein, Chemical, Cell, Primer, Strain
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	constructs = Construct.objects.all()
	antibodies = Antibody.objects.all()
	proteins = Purified_Protein.objects.all()
	chemicals = Chemical.objects.all()
	cells = Cell.objects.all()
	primers = Primer.objects.all()
	strains = Strain.objects.all()
	return render_to_response('reagent_list.html', {'constructs':constructs, 'antibodies':antibodies, 'proteins':proteins, 'chemicals': chemicals, 'cells':cells, 'primers':primers, 'strains':strains },context_instance=RequestContext(request)) 

	
	













