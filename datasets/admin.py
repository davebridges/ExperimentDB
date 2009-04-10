from django.contrib import admin
from experimentdb.datasets.models import SGD_phenotypes

class SGD_phenotypesAdmin(admin.ModelAdmin):
	search_fields = ['Phenotype', 'Gene_Name', 'Chemical', 'Condition']
	list_display = ('Gene_Name', 'Phenotype', 'Chemical', 'Condition')
admin.site.register(SGD_phenotypes, SGD_phenotypesAdmin)

