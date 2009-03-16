from experimentdb.projects.models import Project, SubProject
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
	pass
admin.site.register(Project, ProjectAdmin)

class SubProjectAdmin(admin.ModelAdmin):
	pass
admin.site.register(SubProject, SubProjectAdmin)

