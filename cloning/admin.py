from django.contrib import admin
from experimentdb.cloning.models import Cloning

class CloningAdmin(admin.ModelAdmin):
	pass
admin.site.register(Cloning, CloningAdmin)
