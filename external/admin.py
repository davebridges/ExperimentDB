from django.contrib import admin

from external.models import Reference, Contact, Vendor, AuthorDetails

class ReferenceAdmin(admin.ModelAdmin):
	pass
admin.site.register(Reference, ReferenceAdmin)

class ContactAdmin(admin.ModelAdmin):
	pass
admin.site.register(Contact, ContactAdmin)

class VendorAdmin(admin.ModelAdmin):
	pass
admin.site.register(Vendor, VendorAdmin)

class AuthorDetailsAdmin(admin.ModelAdmin):
	pass
admin.site.register(AuthorDetails, AuthorDetailsAdmin)


