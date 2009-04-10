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
	Reporter  = models.CharField(max_length=250, blank=True, help_text="The protein(s) or RNA(s) used in an experiment to track a process ")
	def __unicode__(self):
		return u'%s, %s' % (self.Gene_Name, self.Phenotype)
