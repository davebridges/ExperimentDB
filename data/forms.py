"""This module contains forms for use in the data package.

The current contents are ExperimentForm and ResultForm, both of which are ModelForms for adding or editing Experiments and Results.
"""

from django import forms

from experimentdb.data.models import Experiment, Result

from django.contrib.admin import widgets


class ExperimentForm(forms.ModelForm):
	"""This is a modelform for the creation and editing of experimental data."""
	class Meta:
		model = Experiment
		
class ResultForm(forms.ModelForm):
	"""This is a modelform for the creation and editing of specific results."""
	class Meta:
		model = Result
		exclude = ['experiment']



