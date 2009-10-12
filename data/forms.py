from django import forms

from django.contrib.admin import widgets


class ExperimentForm(forms.ModelForm):
	class Meta:
		model = Experiment



