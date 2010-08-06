from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from experimentdb.proteins.models import Protein
from experimentdb.data.models import Experiment
from experimentdb.reagents.models import Antibody, Construct, Primer, Purified_Protein
from django.contrib.auth.decorators import login_required
from Bio import Entrez
from Bio import SeqIO
from django.template import RequestContext

@login_required
def index(request):
	protein_list = Protein.objects.order_by('name')
	return render_to_response('protein_index.html', {'protein_list': protein_list},context_instance=RequestContext(request))

@login_required
def detail(request, protein):
	protein = get_object_or_404(Protein, name=protein)
	return render_to_response('protein_detail.html', {'protein': protein, },context_instance=RequestContext(request))

@login_required
def protein_isoform_detail(request, protein_id):
	"""fetch and parse a genbank protein record"""
	#uses the Biopython Entrez module to fetch the genbank protein record
	handle = Entrez.efetch(db="protein", rettype="gb", id=protein_id)
	#uses the Biopython SeqIO module to read the record
	record = SeqIO.read(handle, "gb")
	return render_to_response('protein_isoform_detail.html', {
		'record_id':record.annotations['gi'],
		'name':record.name, 
		'description':record.description, 
		'sequence':record.seq, 
		'species':record.annotations['organism'], 
		'papers':record.annotations['references'], 
		'xrefs':record.dbxrefs,
		'features':record.features}
		,context_instance=RequestContext(request))


