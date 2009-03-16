from experimentdb.proteins.models import Protein
from django.contrib import admin

class ProteinAdmin(admin.ModelAdmin):
	list_display = ('name', 'gene', 'RefSeqProtein', 'RefSeqNucleotide')
admin.site.register(Protein, ProteinAdmin)

