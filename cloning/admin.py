from django.contrib import admin
from experimentdb.cloning.models import Cloning, Mutagenesis

class CloningAdmin(admin.ModelAdmin):
	fieldsets = (
		('General Information', {
			'fields' : ('date_completed', 'construct', 'cloning_type', 'researcher', 'notes')
		}),
		('Cloning Fragment Details', {
			'classes' : ('collapse', ),
			'fields': ('vector', 'insert', 'primer_5prime', 'primer_3prime', )
		}),
		('Digestion Details', {
			'classes' : ('collapse', ),
			'fields': ('restriction_enzyme_5prime', 'vector_restriction_enzyme_5prime','destroyed_5prime','restriction_enzyme_3prime', 'vector_restriction_enzyme_3prime', 'destroyed_3prime', 'vector_CIP', 'ligation_temperaturee', 'ligation_time')
		}),
		('Other Information', {
			'classes' : ('collapse', ),
			'fields': ('gel', 'sequencing')
		}) )
	date_hierarchy = 'date_completed'
	list_filter = ('construct', 'date_completed', 'vector', 'cloning_type', 'researcher')
	list_display = ('construct', 'vector', 'cloning_type', 'date_completed')
admin.site.register(Cloning, CloningAdmin)

class MutagenesisAdmin(admin.ModelAdmin):
	fieldsets = (
		('General Information', {
			'fields' : ('date_completed', 'construct', 'mutation', 'researcher', 'notes', 'method', 'protocol')
		}),
		('PCR Information', {
			'classes' : ('collapse', ),
			'fields': ('template', 'sense_primer', 'antisense_primer')
		}),
		('Result', {
			'classes' : ('collapse', ),
			'fields': ('colonies', 'sequencing')
		}) )
	date_hierarchy = 'date_completed'
	list_filter = ('construct', 'date_completed', 'template','researcher')
	list_display = ('construct', 'mutation', 'template', 'date_completed', 'method')
admin.site.register(Mutagenesis, MutagenesisAdmin)
