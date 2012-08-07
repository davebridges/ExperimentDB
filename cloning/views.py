'''This package controls the views generated for the cloning app'''


from django.views.generic import DetailView

from braces.views import LoginRequiredMixin

from cloning.models import Cloning, Mutagenesis

class CloningDetailView(LoginRequiredMixin, DetailView):
    '''This view is for seeing the details of a Cloning object.'''
    
    model = Cloning
    context_object_name = 'cloning'
    
class MutagenesisDetailView(LoginRequiredMixin, DetailView):
    '''This view is for seeing the details of a Cloning object.'''
    
    model = Mutagenesis
    context_object_name = 'mutagenesis'    