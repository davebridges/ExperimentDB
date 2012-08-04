'''This package controls the views generated for the cloning app'''


from django.views.generic import DetailView

from cloning.models import Cloning

class CloningDetail(DetailView):
    '''This view is for seeing the details of a Cloning object.'''
    
    model = Cloning
    context_object_name = 'cloning'