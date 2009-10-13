from django import forms

from experimentdb.data.models import Experiment

from django.contrib.admin import widgets


class ExperimentForm(forms.ModelForm):
	class Meta:
		model = Experiment



