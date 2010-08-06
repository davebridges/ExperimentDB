"""This module contains forms for use in the data package.

The current contents are ExperimentForm and ResultForm, both of which are ModelForms for adding or editing Experiments and Results.
"""

from django import forms
from django.contrib.admin import widgets
from django.forms.models import inlineformset_factory

from ajax_select.fields import AutoCompleteSelectMultipleField

from experimentdb.data.models import Experiment, Result

class ExperimentForm(forms.ModelForm):
    """This is a modelform for the creation and editing of experimental data."""
    #strain = AutoCompleteSelectMultipleField('strain')
    class Meta:
        model = Experiment
    class Media:
        css = {
		    'all': ('javascript/jquery-ui/css/custom-theme/jquery-ui-1.7.2.custom.css','javascript/jquery-autocomplete/jquery.autocomplete.css', 'css/autocomplete.css')
				}
        js = ('javascript/jquery-1.3.2.js','javascript/jquery-ui/js/jquery-ui-1.7.2.custom.min.js', 'javascript/jquery-autocomplete/jquery.autocomplete.js')


	
		
class ResultForm(forms.ModelForm):
	"""This is a modelform for the creation and editing of specific results."""
	class Meta:
		model = Result
		exclude = ['experiment']
		
ResultFormSet = inlineformset_factory(Experiment, Result, can_delete=True, extra=5)




