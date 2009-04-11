from experimentdb.datasets.models import SGD_GeneNames, SGD_phenotypes, SGD_interactions
from django.shortcuts import render_to_response, get_object_or_404

def sgd_gene_detail(request, gene):
	genename = get_object_or_404(SGD_GeneNames, Locus_name__iexact=gene)
	phenotypes = SGD_phenotypes.objects.filter(Gene_Name=genename)
	interactions_physical_hit = SGD_interactions.objects.filter(Standard_Gene_Name_Hit=genename).filter(Genetic_or_Physical_Interaction='physical interactions')
	interactions_physical_bait = SGD_interactions.objects.filter(Standard_Gene_Name_Bait=genename).filter(Genetic_or_Physical_Interaction='physical interactions')
	interactions_genetic_hit = SGD_interactions.objects.filter(Standard_Gene_Name_Hit=genename).filter(Genetic_or_Physical_Interaction='genetic interactions')
	interactions_genetic_bait = SGD_interactions.objects.filter(Standard_Gene_Name_Bait=genename).filter(Genetic_or_Physical_Interaction='genetic interactions')
	return render_to_response('sgd_gene_detail.html', {'genename':genename, 'phenotypes':phenotypes, 'interactions_physical_hit':interactions_physical_hit, 'interactions_physical_bait':interactions_physical_bait, 'interactions_genetic_hit':interactions_genetic_hit, 'interactions_genetic_bait':interactions_genetic_bait}) 













