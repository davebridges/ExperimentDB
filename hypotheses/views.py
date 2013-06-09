'''This file controls the views for the hypothesis app.'''

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from hypotheses.models import Hypothesis, Process, Manipulation

class HypothesisCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Hypothesis.'''
    
    model = Hypothesis
    template_name = 'hypothesis_form.html'
    permission_required = "hypotheses.create_hypothesis"

class HypothesisDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Hypothesis.'''
    
    model = Hypothesis
    template_name = 'hypothesis_detail.html'
    template_object_name = 'hypothesis'

    
class HypothesisUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Hypothesis.'''
    
    model = Hypothesis
    template_name = 'hypothesis_form.html'
    template_object_name = 'hypothesis'
    permission_required = "hypotheses.update_hypothesis"    
    
class HypothesisDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Hypothesis.'''
    
    model = Hypothesis
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "hypotheses.delete_hypothesis"              
    
class HypothesisList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Hypothesis.'''
    
    model = Hypothesis
    template_name = 'hypothesis_list.html'
    template_object_name = 'hypothesis_list' 
    
class ProcessCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Process.'''
    
    model = Process
    template_name = 'process_form.html'
    permission_required = "hypotheses.create_process"

class ProcessDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Process.'''
    
    model = Process
    template_name = 'process_detail.html'
    template_object_name = 'process'

    
class ProcessUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Process.'''
    
    model = Process
    template_name = 'process_form.html'
    template_object_name = 'process'
    permission_required = "hypotheses.update_process"    
    
class ProcessDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Process.'''
    
    model = Process
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "hypotheses.delete_process"              
    
class ProcessList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Process.'''
    
    model = Process
    template_name = 'process_list.html'
    template_object_name = 'process_list'     


class ManipulationCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Manipulation.'''
    
    model = Manipulation
    template_name = 'manipulation_form.html'
    permission_required = "hypotheses.create_manipulation"

class ManipulationDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Process.'''
    
    model = Manipulation
    template_name = 'manipulation_detail.html'
    template_object_name = 'manipulation'

    
class ManipulationUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Manipulation.'''
    
    model = Manipulation
    template_name = 'manipulation_form.html'
    template_object_name = 'process'
    permission_required = "hypotheses.update_manipulation"    
    
class ManipulationDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Manipulation.'''
    
    model = Manipulation
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "hypotheses.delete_manipulation"              
    
class ManipulationList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Manipulation.'''
    
    model = Manipulation
    template_name = 'manipulation_list.html'
    template_object_name = 'manipulations_list'     
