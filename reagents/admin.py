from experimentdb.reagents.models import Antibody, Chemical, Cell, Purified_Protein, Construct, Primer
from django.contrib import admin

class AntibodyAdmin(admin.ModelAdmin):
	list_display = ('antibody', 'protein_size', 'source_species', 'source', 'catalog')
	fields = ('antibody', 'protein', 'protein_size', 'source_species', 'source', 'catalog', 'notes', 'antibody_slug')
	radio_fields = {"source_species" : admin.HORIZONTAL}
	prepopulated_fields = {"antibody_slug" : ("antibody",)}
admin.site.register(Antibody, AntibodyAdmin)

class ChemicalAdmin(admin.ModelAdmin):
	pass
admin.site.register(Chemical, ChemicalAdmin)

class CellAdmin(admin.ModelAdmin):
	pass
admin.site.register(Cell, CellAdmin)

class ConstructAdmin(admin.ModelAdmin):
	fields = ('construct', 'plasmid', 'protein', 'resistance', 'source','notes', 'contact')
admin.site.register(Construct, ConstructAdmin)

class Purified_ProteinAdmin(admin.ModelAdmin):
	prepopulated_fields = {"name_slug" : ("name",)}
admin.site.register(Purified_Protein, Purified_ProteinAdmin)

class PrimerAdmin(admin.ModelAdmin):
	pass
admin.site.register(Primer, PrimerAdmin)
