from experimentdb.reagents.models import Antibody, Chemical, Cell, Construct, Primer, Strain, Selection, Species
from django.contrib import admin

class AntibodyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Antibody, AntibodyAdmin)

class ChemicalAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chemical, ChemicalAdmin)

class CellAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cell, CellAdmin)

class ConstructAdmin(admin.ModelAdmin):
    pass
admin.site.register(Construct, ConstructAdmin)

class PrimerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Primer, PrimerAdmin)

class StrainAdmin(admin.ModelAdmin):
    pass
admin.site.register(Strain, StrainAdmin)

class SelectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Selection, SelectionAdmin)

class SpeciesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Species, SpeciesAdmin)
