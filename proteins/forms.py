from django import forms
from experimentdb.proteins.models import Protein, ProteinFamily


class ProteinForm(forms.ModelForm):
	protein_family = forms.ModelMultipleChoiceField(
		queryset = ProteinFamily.objects.all(), 
		widget = forms.CheckboxSelectMultiple(),
		)
	class Meta:
		model = Protein



