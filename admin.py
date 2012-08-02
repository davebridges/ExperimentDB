from django.contrib import admin

from proteins.models import Protein
from reagents.models import Antibody, Construct, Chemical, Cell, Purified_Protein
from data.models import Experiment, Result, Protocol
from projects.models import Project, SubProject
from external.models import Contact, Reference

class ProteinAdmin(admin.ModelAdmin):
    pass
admin.site.register(Protein, ProteinAdmin)

class AntibodyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Antibody, AntibodyAdmin)

class ConstructAdmin(admin.ModelAdmin):
    pass
admin.site.register(Construct, ConstructAdmin)

class ChemicalAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chemical, ChemicalAdmin)

class Purified_ProteinAdmin(admin.ModelAdmin):
    pass
admin.site.register(Purified_Protein, Purified_ProteinAdmin)

class ExperimentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Experiment, ExperimentAdmin)

class ResultAdmin(admin.ModelAdmin):
    pass
admin.site.register(Result, ResultAdmin)

class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project, ProjectAdmin)

class SubProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(SubProject, SubProjectAdmin)

class CellAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cell, CellAdmin)

class ProtocolAdmin(admin.ModelAdmin):
    pass
admin.site.register(Protocol, ProtocolAdmin)

class ReferenceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reference, ReferenceAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)
