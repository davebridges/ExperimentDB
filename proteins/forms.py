from django import forms
from experimentdb.proteins.models import Protein, ProteinFamily
from experimentdb.widgets import SelectWithPop


class ProteinForm(forms.ModelForm):
	protein_family = forms.ModelChoiceField(ProteinFamily.objects, widget=SelectWithPop)
	class Meta:
		model = Protein
		
class ProteinFamilyForm(forms.ModelForm):
	class Meta:
		model = ProteinFamily



