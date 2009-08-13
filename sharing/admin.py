from experimentdb.sharing.models import Institution, Laboratory, Recipient, ConstructShipment
from django.contrib import admin

class InstitutionAdmin(admin.ModelAdmin):
	pass
admin.site.register(Institution, InstitutionAdmin)

class LaboratoryAdmin(admin.ModelAdmin):
	pass
admin.site.register(Laboratory, LaboratoryAdmin)

class RecipientAdmin(admin.ModelAdmin):
	pass
admin.site.register(Recipient, RecipientAdmin)

class ConstructShipmentAdmin(admin.ModelAdmin):
	list_display = ('ship_date', 'recipient',)
admin.site.register(ConstructShipment, ConstructShipmentAdmin)

