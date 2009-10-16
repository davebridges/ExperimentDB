from django import forms

from experimentdb.data.models import Experiment, Result

from django.contrib.admin import widgets


class ExperimentForm(forms.ModelForm):
	class Meta:
		model = Experiment
		
class ResultForm(forms.ModelForm):
	class Meta:
		model = Result
		exclude = ['experiment']



