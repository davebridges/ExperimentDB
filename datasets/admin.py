from django.contrib import admin
from experimentdb.datasets.models import SGD_phenotypes, SGD_interactions

class SGD_phenotypesAdmin(admin.ModelAdmin):
	search_fields = ['Phenotype', 'Gene_Name', 'Chemical', 'Condition']
	list_display = ('Gene_Name', 'Phenotype', 'Chemical', 'Condition')
admin.site.register(SGD_phenotypes, SGD_phenotypesAdmin)

class SGD_interactionsAdmin(admin.ModelAdmin):
	search_fields = ['Standard_Gene_Name_Bait', 'Feature_Name_Bait', 'Standard_Gene_Name_Hit', 'Feature_Name_Hit']
	list_display = ('Standard_Gene_Name_Bait', 'Standard_Gene_Name_Hit', 'Experiment_Type', 'Genetic_or_Physical_Interaction', 'Manually_Curated_or_High_Throughput')
	list_filter = ('Genetic_or_Physical_Interaction', 'Manually_Curated_or_High_Throughput', 'Experiment_Type')
admin.site.register(SGD_interactions, SGD_interactionsAdmin)

