from django.contrib import admin

from projects.models import Project, SubProject

class ProjectAdmin(admin.ModelAdmin):
	pass
admin.site.register(Project, ProjectAdmin)

class SubProjectAdmin(admin.ModelAdmin):
	pass
admin.site.register(SubProject, SubProjectAdmin)

