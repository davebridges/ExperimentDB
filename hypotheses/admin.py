"""This module defines the admin interface for the hypotheses application.

Currently each of the following models has the default admin interface:

* Hypothesis
* Manipulation
* Effect
* Process
* Entity
* Context
"""

from experimentdb.hypotheses.models import Hypothesis, Effect, Manipulation, Process, Entity, Evidence, CitationType, Context
from django.contrib import admin

class HypothesisAdmin(admin.ModelAdmin):
	pass
admin.site.register(Hypothesis, HypothesisAdmin)

class ManipulationAdmin(admin.ModelAdmin):
	pass
admin.site.register(Manipulation, ManipulationAdmin)

class EffectAdmin(admin.ModelAdmin):
	pass
admin.site.register(Effect, EffectAdmin)

class ProcessAdmin(admin.ModelAdmin):
	pass
admin.site.register(Process, ProcessAdmin)

class EntityAdmin(admin.ModelAdmin):
	pass
admin.site.register(Entity, EntityAdmin)

class EvidenceAdmin(admin.ModelAdmin):
	pass
admin.site.register(Evidence, EvidenceAdmin)

class CitationTypeAdmin(admin.ModelAdmin):
	pass
admin.site.register(CitationType, CitationTypeAdmin)

class ContextAdmin(admin.ModelAdmin):
	pass
admin.site.register(Context, ContextAdmin)