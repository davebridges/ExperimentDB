"""This module contains forms for use in the data package.

The current contents are ExperimentForm and ResultForm, both of which are ModelForms for adding or editing Experiments and Results.
"""

from django import forms
from django.contrib.admin import widgets
from django.forms.models import inlineformset_factory

from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteSelectField

from experimentdb.data.models import Experiment, Result

class ExperimentForm(forms.ModelForm):
    """This is a modelform for the creation and editing of experimental data."""
    antibodies = AutoCompleteSelectMultipleField('antibody', required=False)
    constructs = AutoCompleteSelectMultipleField('construct', required=False)	
    cellline = AutoCompleteSelectMultipleField('cell', required=False)
    chemicals = AutoCompleteSelectMultipleField('chemical', required=False)
    siRNA = AutoCompleteSelectMultipleField('siRNA', required=False)	
    strain = AutoCompleteSelectMultipleField('strain', required=False)	
    protein = AutoCompleteSelectMultipleField('protein', required=False)		
    protocol = AutoCompleteSelectMultipleField('protocol', required=False)	
    class Meta:
        model = Experiment
    class Media:
        """This form requires both a css and javascript file for the autocomplete function.
        
        The css/autocomplete.css file has been customized to match the vader theme."""
        css = {
		    'all': ('css/autocomplete.css',),
              }
        js = ("js/jquery-autocomplete/jquery.autocomplete.js",)


	
		
class ResultForm(forms.ModelForm):
	"""This is a modelform for the creation and editing of specific results."""
	class Meta:
		model = Result
		exclude = ['experiment']
		
ResultFormSet = inlineformset_factory(Experiment, Result, can_delete=True, extra=5)




