from django.db import models

class SGD_phenotypes(models.Model):
#schema is described in http://wiki.yeastgenome.org/index.php/Specification_for_New_Interactions_and_Phenotype_FTP_files
#download updated phenotypes ftp://genome-ftp.stanford.edu/pub/yeast/literature_curation/phenotype_data.tab
	Feature_Name = models.CharField(max_length=20, help_text="The feature name of the gene") 
	Feature_Type = models.CharField(max_length=50, help_text="The feature type of the gene")
	Gene_Name = models.CharField(max_length= 50, blank=True, help_text="The standard name of the gene")
	SGDID = models.CharField(max_length= 15, help_text="The SGDID of the gene")
	Reference = models.CharField(max_length= 50, help_text ="PMID: #### SGD_REF: #### (separated by pipe)(one reference per row")
	Experiment_Type  = models.CharField(max_length=250, help_text="The method used to detect and analyze the phenotype")
	Mutant_Type  = models.CharField(max_length=50, help_text="Description of the impact of the mutation on activity of the gene product")
	Allele  = models.CharField(max_length=250, blank=True, help_text="Allele name and description, if applicable")
	Strain_Background   = models.CharField(max_length=50, blank=True, help_text="Genetic background in which the phenotype was analyzed")
	Phenotype   = models.CharField(max_length=100, help_text="The feature observed and the direction of change relative to wild type")
	Chemical  = models.CharField(max_length=150, blank=True, help_text="Any chemicals relevant to the phenotype")
	Condition  = models.CharField(max_length=250, help_text="Condition under which the phenotype was observed") 
	Details  = models.CharField(max_length=250, blank=True, help_text="Details about the phenotype")
	Reporter  = models.CharField(max_length=250, blank=True, help_text="The protein(s) or RNA(s) used in an experiment to track a process")
	def __unicode__(self):
		return u'%s, %s' % (self.Gene_Name, self.Phenotype)

class SGD_interactions(models.Model):
	Feature_Name_Bait = models.CharField(max_length=50, help_text="The feature name of the gene used as the bait")
	Standard_Gene_Name_Bait = models.CharField(max_length=50, help_text="The standard gene name of the gene used as the bait", blank=True)
	Feature_Name_Hit = models.CharField(max_length=50, help_text="The feature name of the gene that interacts with the bait")
	Standard_Gene_Name_Hit = models.CharField(max_length=50, help_text="The standard gene name of the gene that interacts with the bait", blank=True)
	Experiment_Type = models.CharField(max_length=50, help_text="A description of the experimental used to identify the interaction")
	Genetic_or_Physical_Interaction = models.CharField(max_length=100, help_text="Indicates whether the experimental method is a genetic or physical interaction")
	Source = models.CharField(max_length=50, help_text="Lists the database source for the interaction")
	Manually_Curated_or_High_Throughput = models.CharField(max_length=50, help_text="Lists whether the interaction was manually curated from a publication or added as part of a high-throughput dataset")
	Notes = models.TextField(max_length=250, help_text="Free text field that contains additional information about the interaction", blank=True)
	Phenotype = models.CharField(max_length=50, help_text="Contains the phenotype of the interaction", blank=True)
	Reference = models.CharField(max_length=100, help_text="Lists the identifiers for the reference as an SGDID (SGD_REF:) or a PubMed ID (PMID:)")
	Citation = models.TextField(max_length=500, help_text = "Lists the citation for the reference")
	def __unicode__(self):
		return u'%s with %s' % (self.Feature_Name_Bait, self.Feature_Name_Hit)

