'''This app contains the views for the external app.

'''
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from external.models import Reference

class PaperListView(ListView):
	'''This class generates the view for papers located at **/references/**
	
	It is subclasses for lab and interesting papers.'''

	model = Reference
	template_name = "paper-list.html"


class LaboratoryPaperListView(PaperListView):
    '''This class generates the view for laboratory-papers located at **/references/lab-papers/**.
    
    This is filtered based on whether the publication is marked as laboratory_paper = True.
    '''
    queryset = Reference.objects.filter(laboratory_paper=True)
    
    def get_context_data(self, **kwargs):
        '''This method adds to the context the paper-list-type  = interesting.'''
        context = super(LaboratoryPaperList, self).get_context_data(**kwargs)
        context['paper-list-type'] = "laboratory"
        return context    
    
class InterestingPaperListView(PaperListView):
    '''This class generates the view for interesting-papers located at **/references/interesting-papers/**.
    
    This is filtered based on whether the publication is marked as interesting_paper = True.
    '''
    queryset = Reference.objects.filter(interesting_paper=True)
    
    def get_context_data(self, **kwargs):
        '''This method adds to the context the paper-list-type  = interesting.'''
        context = super(LaboratoryPaperList, self).get_context_data(**kwargs)
        context['paper-list-type'] = "interesting"
        return context       

class PaperDetailView(DetailView):
    '''This class generates the view for paper-details located at **/references/<title_slug>**.
    
    '''
    model = Reference
    slug_field = "title_slug"
    slug_url_kwarg = "title_slug"
    template_name = "paper-detail.html"

