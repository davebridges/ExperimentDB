"""This package contains views for the reagents app."""

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from reagents.models import Construct, Antibody, Chemical, Cell, Primer, Strain, License, AnimalStrain

@login_required
def index(request):
	constructs = Construct.objects.all()
	antibodies = Antibody.objects.all()
	chemicals = Chemical.objects.all()
	cells = Cell.objects.all()
	primers = Primer.objects.all()
	strains = Strain.objects.all()
        animals = AnimalStrain.objects.all()
	return render_to_response('reagent_list.html', {'constructs':constructs, 
                                                        'antibodies':antibodies, 
                                                        'chemicals': chemicals, 
                                                        'cells':cells, 
                                                        'primers':primers, 
                                                        'strains':strains,
                                                        'animals':animals
                                  },context_instance=RequestContext(request)) 

	
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


class ConstructCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Construct.'''
    
    model = Construct
    template_name = 'construct_form.html'
    permission_required = "reagents.create_construct"

class ConstructDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Construct.'''
    
    model = Construct
    template_name = 'construct_detail.html'
    template_object_name = 'construct'

    
class ConstructUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Construct.'''
    
    model = Construct
    template_name = 'construct_form.html'
    template_object_name = 'construct'
    permission_required = "reagents.update_construct"    
    
class ConstructDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Construct.'''
    
    model = Construct
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "reagents.delete_construct"              
    success_url = reverse_lazy('construct-list')   

class ConstructList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Construct.'''
    
    model = Construct
    template_name = 'construct_list.html'
    template_object_name = 'construct_list' 
    
class AntibodyCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Antibody.'''
    
    model = Antibody
    template_name = 'antibody_form.html'
    permission_required = "reagents.create_antibody"

class AntibodyDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Antibody.'''
    
    model = Antibody
    template_name = 'antibody_detail.html'
    template_object_name = 'antibody'

    
class AntibodyUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Antibody.'''
    
    model = Antibody
    template_name = 'antibody_form.html'
    template_object_name = 'antibody'
    permission_required = "reagents.update_antibody"    
    
class AntibodyDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Antibody.'''
    
    model = Antibody
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "reagents.delete_antibody"              
    success_url	= reverse_lazy('antibody-list')

class AntibodyList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Antibody.'''
    
    model = Antibody
    template_name = 'antibody_list.html'
    template_object_name = 'antibody_list'     
    
class ChemicalCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Chemical.'''
    
    model = Chemical
    template_name = 'chemical_form.html'
    permission_required = "reagents.create_chemical"

class ChemicalDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Chemical.'''
    
    model = Chemical
    template_name = 'chemical_detail.html'
    template_object_name = 'chemical'

    
class ChemicalUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Chemical.'''
    
    model = Chemical
    template_name = 'chemical_form.html'
    template_object_name = 'chemical'
    permission_required = "reagents.update_chemical"    
    
class ChemicalDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Chemical.'''
    
    model = Chemical
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "reagents.delete_chemical"              
    success_url	= reverse_lazy('chemical-list')
    
class ChemicalList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Chemical.'''
    
    model = Chemical
    template_name = 'chemical_list.html'
    template_object_name = 'chemical_list' 
    
class CellCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Cell.'''
    
    model = Cell
    template_name = 'cell_form.html'
    permission_required = "reagents.create_cell"

class CellDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Cell.'''
    
    model = Cell
    template_name = 'cell_detail.html'
    template_object_name = 'cell'

    
class CellUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Cell.'''
    
    model = Cell
    template_name = 'cell_form.html'
    template_object_name = 'cell'
    permission_required = "reagents.update_cell"    
    
class CellDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Cell.'''
    
    model = Cell
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "reagents.delete_cell"              
    success_url	= reverse_lazy('cell-list')
    
class CellList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Cell.'''
    
    model = Cell
    template_name = 'cell_list.html'
    template_object_name = 'cell_list' 
    
class PrimerCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Primer.'''
    
    model = Primer
    template_name = 'primer_form.html'
    permission_required = "reagents.create_primer"

class PrimerDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Primer.'''
    
    model = Primer
    template_name = 'primer_detail.html'
    template_object_name = 'primer'

    
class PrimerUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Primer.'''
    
    model = Primer
    template_name = 'primer_form.html'
    template_object_name = 'primer'
    permission_required = "reagents.update_primer"    
    
class PrimerDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Primer.'''
    
    model = Primer
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "reagents.delete_primer"              
    success_url	= reverse_lazy('primer-list')
    
class PrimerList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Primer.'''
    
    model = Primer
    template_name = 'primer_list.html'
    template_object_name = 'primer_list' 
    
class StrainCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Strain.'''
    
    model = Strain
    template_name = 'strain_form.html'
    permission_required = "reagents.create_strain"

class StrainDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Strain.'''
    
    model = Strain
    template_name = 'strain_detail.html'
    template_object_name = 'strain'

    
class StrainUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Strain.'''
    
    model = Strain
    template_name = 'strain_form.html'
    template_object_name = 'strain'
    permission_required = "reagents.update_strain"    
    
class StrainDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Strain.'''
    
    model = Strain
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "reagents.delete_strain"              
    success_url	= reverse_lazy('strain-list')
    
class StrainList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Strain.'''
    
    model = Strain
    template_name = 'strain_list.html'
    template_object_name = 'strain_list' 
    
class LicenseCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new License.'''
    
    model = License
    template_name = 'license_form.html'
    permission_required = "reagents.create_license"

class LicenseDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing License.'''
    
    model = License
    template_name = 'license_detail.html'
    template_object_name = 'license'

    
class LicenseUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a License.'''
    
    model = License
    template_name = 'license_form.html'
    template_object_name = 'license'
    permission_required = "reagents.update_license"    
    
class LicenseDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a License.'''
    
    model = License
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "reagents.delete_license"              
    success_url	= reverse_lazy('license-list')
    
class LicenseList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of License.'''
    
    model = License
    template_name = 'license_list.html'
    template_object_name = 'license_list'                     

class AnimalStrainCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new AnimalStrain.'''
    
    model = AnimalStrain
    template_name = 'animalstrain_form.html'
    permission_required = "reagents.create_animalstrain"

class AnimalStrainDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing AnimalStrain.'''
    
    model = AnimalStrain
    template_name = 'animalstrain_detail.html'
    template_object_name = 'animalstrain'

    
class AnimalStrainUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a AnimalStrain.'''
    
    model = AnimalStrain
    template_name = 'animalstrain_form.html'
    template_object_name = 'animalstrain'
    permission_required = "reagents.update_animalstrain"    
    
class AnimalStrainDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a AnimalModel.'''
    
    model = AnimalStrain
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "reagents.delete_animalstrain"              
    success_url = reverse_lazy('animal-list')   

class AnimalStrainList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of AnimalStrain.'''
    
    model = AnimalStrain
    template_name = 'animalstrain_list.html'
    template_object_name = 'animalstrain_list' 
