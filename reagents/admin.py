from experimentdb.reagents.models import Antibody, Chemical, Cell, Purified_Protein, Construct, Primer, Strain, Selection
from django.contrib import admin

class AntibodyAdmin(admin.ModelAdmin):
	list_display = ('antibody', 'protein_size', 'source_species', 'source', 'catalog')
	fields = ('antibody', 'protein', 'protein_size', 'source_species', 'source', 'vendor', 'location', 'catalog', 'notes', 'antibody_slug')
	radio_fields = {"source_species" : admin.HORIZONTAL}
	prepopulated_fields = {"antibody_slug" : ("antibody",)}
admin.site.register(Antibody, AntibodyAdmin)

class ChemicalAdmin(admin.ModelAdmin):
	list_display = ('chemical', 'source')
admin.site.register(Chemical, ChemicalAdmin)

class CellAdmin(admin.ModelAdmin):
	list_display = ('description', 'species', 'source')
	fields = ('description', 'species', 'notes', 'cellline')
	prepopulated_fields = {"cellline" : ("description",)}
admin.site.register(Cell, CellAdmin)

class ConstructAdmin(admin.ModelAdmin):
	fields = ('construct', 'plasmid', 'protein', 'resistance', 'source', 'location', 'box', 'sequencing_contig', 'sequenced_object','notes', 'contact')
	list_display = ('construct', 'plasmid', 'location', 'box', 'resistance', 'source')
	list_filter = ('protein', 'plasmid')
admin.site.register(Construct, ConstructAdmin)

class Purified_ProteinAdmin(admin.ModelAdmin):
	prepopulated_fields = {"name_slug" : ("name",)}
	list_display = ('name', 'tag', 'construct')
	list_filter = ('tag', 'protein', 'construct')
admin.site.register(Purified_Protein, Purified_ProteinAdmin)

class PrimerAdmin(admin.ModelAdmin):
	list_display = ('primer', 'primer_type', 'date_ordered', 'vendor', 'protein', 'sequence')
	list_filter = ('primer_type', 'protein')
admin.site.register(Primer, PrimerAdmin)

class StrainAdmin(admin.ModelAdmin):
	pass
admin.site.register(Strain, StrainAdmin)

class SelectionAdmin(admin.ModelAdmin):
	pass
admin.site.register(Selection, SelectionAdmin)