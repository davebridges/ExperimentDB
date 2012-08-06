from django.contrib import admin

from proteins.models import ProteinFamily, Protein, ProteinDetail


class ProteinFamilyAdmin(admin.ModelAdmin):
	pass
admin.site.register(ProteinFamily, ProteinFamilyAdmin)

class ProteinAdmin(admin.ModelAdmin):
	list_display = ('name',)
admin.site.register(Protein, ProteinAdmin)

class ProteinDetailAdmin(admin.ModelAdmin):
	list_display = ('name', 'protein', 'gene', 'RefSeqProtein', 'RefSeqNucleotide')
	list_filter = ('protein', )
admin.site.register(ProteinDetail, ProteinDetailAdmin)