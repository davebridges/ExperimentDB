'''This package contains view classes and functions for the hypotheses app.

'''

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from hypotheses.models import Evidence

class EvidenceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    '''This view is for creating new :class:`~hypotheses.models.Evidence` objects.'''
    
    model = Evidence
    permission_required = "hypotheses.add_evidence"
    context_object_name = 'evidence'
    template_name = 'evidence_form.html'
    
class EvidenceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    '''This view is for updating :class:`~hypotheses.models.Evidence` objects.'''
    
    model = Evidence
    permission_required = "hypotheses.change_evidence"
    context_object_name = 'evidence'
    template_name = 'evidence_form.html'  

class EvidenceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''This view is for deleting :class:`~hypotheses.models.Evidence` objects.'''

    model = Evidence   
    permission_required = "hypotheses.delete_evidence" 
    template_name = 'confirm_delete.html'
        