from django.contrib import admin
from experimentdb.cloning.models import Cloning, Mutagenesis

class CloningAdmin(admin.ModelAdmin):
	pass
admin.site.register(Cloning, CloningAdmin)

class MutagenesisAdmin(admin.ModelAdmin):
	pass
admin.site.register(Mutagenesis, MutagenesisAdmin)
