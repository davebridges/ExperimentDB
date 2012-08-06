from django import forms

from proteins.models import Protein, ProteinFamily

class ProteinForm(forms.ModelForm):
	class Meta:
		model = Protein
		
class ProteinFamilyForm(forms.ModelForm):
	class Meta:
		model = ProteinFamily



