from django.db import models

class ProteinFamily(models.Model):
	name = models.CharField(max_length=50)
	notes = models.TextField(max_length=500, blank=True)
	def __unicode__(self):
		return '%s' % self.name
	class Meta:
		ordering = ['name']
		verbose_name = "Protein Family"
		verbose_name_plural = "Protein Families"

class Protein(models.Model):
	protein_family = models.ManyToManyField('ProteinFamily')
	name = models.CharField(max_length=25)
	def __unicode__(self):
		return u'%s' % self.name
	def get_absolute_url(self):
		return "/protein/%i/" % self.id
	class Meta:
		ordering = ['name']
		verbose_name_plural = "Proteins"
		
class Species(models.Model):
	common_name = models.CharField(max_length=50)
	scientific_name = models.CharField(max_length=50, blank=True)
	taxonomy_id = models.IntegerField(blank=True)
	def __unicode__(self):
		return '%s' % self.common_name
	class Meta:
		verbose_name_plural = "Species"
	
		
class ProteinDetail(models.Model):
	name = models.CharField(max_length=50, help_text="Our Name for the Protein")
	protein = models.ForeignKey('Protein')
	gene = models.CharField(max_length=10, blank=True)
	species = models.ForeignKey('Species')
	geneID = models.IntegerField(blank=True)
	RefSeqProtein = models.CharField(max_length=15, blank=True, verbose_name="Protein Sequence (RefSeq)")
	RefSeqProtein_gi = models.IntegerField(max_length=20, blank=True)
	RefSeqNucleotide = models.CharField(max_length=15, blank=True, verbose_name="Nucleotide Sequence (RefSeq)")
	RefSeqNucleotide_gi = models.IntegerField(max_length=10, blank=True)
	WormBaseID = models.CharField(max_length=50, blank=True)
	FlyBaseID = models.CharField(max_length=50, blank=True)
	SGD_ID = models.CharField(max_length=25, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	def __unicode__(self):
		return u'%s' % self.name
	class Meta:
		verbose_name_plural = "Protein Isoforms"
	
