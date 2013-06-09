
'''This package controls the views generated for the proteins app'''


from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from reagents.models import Antibody, Construct, Primer
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from Bio import Entrez
from Bio import SeqIO

from proteins.models import Protein, ProteinFamily
from proteins.forms import ProteinFamilyForm
from data.models import Experiment

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
		
@login_required
def newProteinFamily(request):
	return handlePopAdd(request, ProteinFamilyForm, 'protein_family')
    
class ProteinCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Protein.'''
    
    model = Protein
    template_name = 'protein_form.html'
    permission_required = "proteins.create_protein"

class ProteinDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Protein.'''
    
    model = Protein
    template_name = 'protein_detail.html'
    template_object_name = 'protein'

    
class ProteinUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Protein.'''
    
    model = Protein
    template_name = 'protein_form.html'
    template_object_name = 'protein'
    permission_required = "proteins.update_protein"    
    
class ProteinDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Protein.'''
    
    model = Protein
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "proteins.delete_protein"              
    
class ProteinList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Protein.'''
    
    model = Protein
    template_name = 'protein_list.html'
    template_object_name = 'protein_list' 
    
class ProteinFamilyCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new ProteinFamily.'''
    
    model = ProteinFamily
    template_name = 'proteinfamily_form.html'
    permission_required = "proteins.create_proteinfamily"

class ProteinFamilyDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing ProteinFamily.'''
    
    model = ProteinFamily
    template_name = 'proteinfamily_detail.html'
    template_object_name = 'proteinfamily'

    
class ProteinFamilyUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a ProteinFamily.'''
    
    model = ProteinFamily
    template_name = 'proteinfamily_form.html'
    template_object_name = 'proteinfamily'
    permission_required = "proteins.update_proteinfamily"    
    
class ProteinFamilyDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a ProteinFamily.'''
    
    model = ProteinFamily
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "proteins.delete_proteinfamily"              
    
class ProteinFamilyList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of ProteinFamily.'''
    
    model = ProteinFamily
    template_name = 'proteinfamily_list.html'
    template_object_name = 'proteinfamily_list'         

