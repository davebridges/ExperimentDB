from django.db import models

class Protein(models.Model):
	name = models.CharField(max_length=10)
	gene = models.CharField(max_length=10, blank=True)
	RefSeqProtein = models.CharField(max_length=10, blank=True)
	RefSeqNucleotide = models.CharField(max_length=10, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	def __unicode__(self):
		return u'%s' % self.name
	def get_absolute_url(self):
		return "/protein/%i/" % self.id
	class Meta:
		ordering = ['name']

	
