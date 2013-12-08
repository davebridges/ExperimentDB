from django.db import models

class ProteinFamily(models.Model):
	name = models.CharField(max_length=50)
	notes = models.TextField(max_length=500, blank=True)
	def __unicode__(self):
		return '%s' % self.name
	@models.permalink
	def get_absolute_url(self):
		return ('protein-family-detail', [int(self.id)])		
	class Meta:
		ordering = ['name']
		verbose_name = "Protein Family"
		verbose_name_plural = "Protein Families"

class Protein(models.Model):
    '''This object contains protein information.
    
    A Protein object is a generic link to all isoforms/splice variants and species of a protein.
    The intent is so that a protein can be referred to generically in a species and isoform independent manner.
    '''
    protein_family = models.ManyToManyField('ProteinFamily', blank=True, null=True)
    name = models.CharField(max_length=25, help_text="This is our generic, isoform and species agnostic name for the protein")

    def __unicode__(self):
        return u'%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('protein-detail', [int(self.id)])

    class Meta:
		ordering = ['name']
		verbose_name_plural = "Proteins"
		
		
class ProteinDetail(models.Model):
    '''The protein detail contains isoform and species level detail of a protein.
    
    Since a Protein object is a generic link to all isoforms/splice variants and species of a protein this allows for links to the specific protein details when needed.'''
    
    name = models.CharField(max_length=50, help_text="Our name for the protein, should include the species and isoform/splice variant")
    protein = models.ForeignKey('Protein')
    gene = models.CharField(max_length=10, blank=True)
    species = models.ForeignKey('reagents.Species', blank=True, null=True)
    geneID = models.IntegerField(blank=True, null=True)
    RefSeqProtein = models.CharField(max_length=15, blank=True, null=True, verbose_name="Protein ID (RefSeq)")
    RefSeqProtein_gi = models.IntegerField(max_length=20, blank=True, null=True)
    RefSeqNucleotide = models.CharField(max_length=15, blank=True, null=True, verbose_name="Nucleotide ID (RefSeq)")
    RefSeqNucleotide_gi = models.IntegerField(max_length=10, blank=True, null=True)
    WormBaseID = models.CharField(max_length=50, blank=True, null=True)
    FlyBaseID = models.CharField(max_length=50, blank=True, null=True)
    SGD_ID = models.CharField(max_length=25, blank=True, null=True)
    public = models.BooleanField()
    published = models.BooleanField()

    def __unicode__(self):
        return u'%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        '''The permalink for a protein detail is regulated by the protein-isoform-detail link.'''
        return ('protein-isoform-detail', [int(self.id)])
        
    class Meta:
		verbose_name_plural = "Protein Isoforms"
	
