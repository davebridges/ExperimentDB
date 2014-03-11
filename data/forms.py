"""This module contains forms for use in the data package.

The current contents are ExperimentForm and ResultForm, both of which are ModelForms for adding or editing Experiments and Results.
"""

from django import forms
from django.contrib.admin import widgets
from django.forms.models import inlineformset_factory

from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteSelectField
from ajax_select import make_ajax_field

from data.models import Experiment, RawDataFile, ResultFigure

class ExperimentForm(forms.ModelForm):
    """This is a modelform for the creation and editing of experimental data."""
    antibodies = make_ajax_field(Experiment, 'antibodies', 'antibody')
    constructs = make_ajax_field(Experiment, 'constructs', 'construct')	
    cellline = make_ajax_field(Experiment, 'cellline', 'cell')
    chemicals = make_ajax_field(Experiment, 'chemicals', 'chemical')
    siRNA = make_ajax_field(Experiment, 'siRNA', 'siRNA')	
    strain = make_ajax_field(Experiment, 'strain', 'strain')	
    protein = make_ajax_field(Experiment, 'protein', 'protein')		
    protocol = make_ajax_field(Experiment, 'protocol', 'protocol')	

    class Meta:
        model = Experiment
	
class RawDataFileForm(forms.ModelForm):
	"""This is a modelform for the adding of raw data."""
	class Meta:
		model = RawDataFile
                exclude =['experiment','public','published']


class FigureFileForm(forms.ModelForm):
	"""This is a modelform for the adding of a figure."""
	class Meta:
		model = ResultFigure
                exclude =['experiment','public','published']
