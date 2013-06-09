'''This package controls the views generated for the cloning app'''


from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from cloning.models import Cloning, Mutagenesis
    
class MutagenesisCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Mutagenesis.'''
    
    model = Mutagenesis
    template_name = 'mutagenesis_form.html'
    permission_required = "cloning.create_mutagenesis"

class MutagenesisDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Mutagenesis.'''
    
    model = Mutagenesis
    template_name = 'mutagenesis_detail.html'
    template_object_name = 'mutagenesis'

    
class MutagenesisUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Mutagenesis.'''
    
    model = Mutagenesis
    template_name = 'mutagenesis_form.html'
    template_object_name = 'mutagenesis'
    permission_required = "cloning.update_mutagenesis"    
    
class MutagenesisDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Mutagenesis.'''
    
    model = Mutagenesis
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "cloning.delete_mutagenesis"              
    
class MutagenesisList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Mutagenesis.'''
    
    model = Mutagenesis
    template_name = 'mutagenesis_list.html'
    template_object_name = 'mutagenesis_list' 
    
class CloningCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Cloning.'''
    
    model = Cloning
    template_name = 'cloning_form.html'
    permission_required = "cloning.create_cloning"

class CloningDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Cloning.'''
    
    model = Cloning
    template_name = 'cloning_detail.html'
    template_object_name = 'cloning'

    
class CloningUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Cloning.'''
    
    model = Cloning
    template_name = 'cloning_form.html'
    template_object_name = 'cloning'
    permission_required = "cloning.update_cloning"    
    
class CloningDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Cloning.'''
    
    model = Cloning
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "cloning.delete_cloning"              
    
class CloningList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Cloning.'''
    
    model = Cloning
    template_name = 'cloning_list.html'
    template_object_name = 'cloning_list'         