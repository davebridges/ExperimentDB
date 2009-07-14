from django.contrib import admin
from experimentdb.datasets.models import SGD_phenotypes, SGD_interactions, SGD_GeneNames, PI35P2_Binding_Screen_SP

class SGD_phenotypesAdmin(admin.ModelAdmin):
	search_fields = ['Phenotype', 'Gene_Name', 'Chemical', 'Condition']
	list_display = ('Gene_Name', 'Phenotype', 'Chemical', 'Condition')
admin.site.register(SGD_phenotypes, SGD_phenotypesAdmin)

class SGD_interactionsAdmin(admin.ModelAdmin):
	search_fields = ['Standard_Gene_Name_Bait', 'Feature_Name_Bait', 'Standard_Gene_Name_Hit', 'Feature_Name_Hit']
	list_display = ('Standard_Gene_Name_Bait', 'Standard_Gene_Name_Hit', 'Experiment_Type', 'Genetic_or_Physical_Interaction', 'Manually_Curated_or_High_Throughput')
	list_filter = ('Genetic_or_Physical_Interaction', 'Manually_Curated_or_High_Throughput', 'Experiment_Type')
admin.site.register(SGD_interactions, SGD_interactionsAdmin)

class SGD_GeneNamesAdmin(admin.ModelAdmin):
	search_fields = ['Locus_name', 'Other_name', 'Description', 'ORF_name', 'Phenotype', 'Gene_product']
	list_display = ('Locus_name', 'Other_name', 'Description', 'Gene_product')
admin.site.register(SGD_GeneNames, SGD_GeneNamesAdmin)

class PI35P2_Binding_Screen_SPAdmin(admin.ModelAdmin):
	list_display = ('Gene_Name', 'Gain_of_Function', 'Loss_of_Function', 'Candidate', 'Comments')
	search_fields = ('Gene_Name',)
	list_filter = ('Gain_of_Function', 'Loss_of_Function')
admin.site.register(PI35P2_Binding_Screen_SP, PI35P2_Binding_Screen_SPAdmin)

