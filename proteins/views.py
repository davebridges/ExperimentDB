from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from experimentdb.proteins.models import Protein
from experimentdb.data.models import Experiment
from experimentdb.reagents.models import Antibody, Construct, Primer, Purified_Protein
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	protein_list = Protein.objects.order_by('name')
	return render_to_response('protein_index.html', {'protein_list': protein_list})

@login_required
def detail(request, protein):
	protein = get_object_or_404(Protein, name=protein)
	antibodies = Antibody.objects.filter(protein = protein)
	constructs = Construct.objects.filter(protein = protein)
	purified_proteins = Purified_Protein.objects.filter(protein = protein)
	primers = Primer.objects.filter(protein = protein)
	experiment_protein = Experiment.objects.filter(protein=protein)
	return render_to_response('protein_detail.html', {'protein': protein, 'experiment_protein':experiment_protein, 'antibodies':antibodies, 'constructs':constructs, 'purified_proteins':purified_proteins, 'primers':primers})


