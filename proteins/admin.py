from experimentdb.proteins.models import ProteinFamily, Protein, Species, ProteinDetail
from django.contrib import admin

class ProteinFamilyAdmin(admin.ModelAdmin):
	pass
admin.site.register(ProteinFamily, ProteinFamilyAdmin)

class ProteinAdmin(admin.ModelAdmin):
	list_display = ('name',)
admin.site.register(Protein, ProteinAdmin)

class SpeciesAdmin(admin.ModelAdmin):
	pass
admin.site.register(Species, SpeciesAdmin)

class ProteinDetailAdmin(admin.ModelAdmin):
	list_display = ('name', 'protein', 'gene', 'RefSeqProtein', 'RefSeqNucleotide')
	list_filter = ('protein', )
admin.site.register(ProteinDetail, ProteinDetailAdmin)