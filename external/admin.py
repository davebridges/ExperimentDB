from experimentdb.external.models import Reference, Contact, Vendor
from django.contrib import admin

class ReferenceAdmin(admin.ModelAdmin):
	pass
admin.site.register(Reference, ReferenceAdmin)

class ContactAdmin(admin.ModelAdmin):
	pass
admin.site.register(Contact, ContactAdmin)

class VendorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Vendor, VendorAdmin)


