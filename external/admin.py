from django.contrib import admin

from external.models import Reference, Contact, Vendor

class ReferenceAdmin(admin.ModelAdmin):
	pass
admin.site.register(Reference, ReferenceAdmin)

class ContactAdmin(admin.ModelAdmin):
	pass
admin.site.register(Contact, ContactAdmin)

class VendorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Vendor, VendorAdmin)


