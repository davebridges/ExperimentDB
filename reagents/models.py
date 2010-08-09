from django.db import models

from experimentdb.proteins.models import Protein
from experimentdb.external.models import Contact, Reference, Vendor
#from experimentdb.data.models import Experiment, Protocol, Result



SPECIES = (
	('rabbit', 'rabbit'),
	('mouse', 'mouse'),
	('human', 'human'),
	('monkey', 'monkey'),
	('goat', 'goat'),
	('sheep', 'sheep'),
	('rat', 'rat'),
	('fly', 'fly'),
)

PRIMER_TYPE = (
	('cloning', 'cloning'),
	('sequencing', 'sequencing'),
	('RT-PCR', 'RT-PCR'),
	('siRNA', 'siRNA'),
	('genotyping', 'Genotyping'),
	('dsRNA', 'dsRNA Amplification'),
	('mutagenesis', 'mutagenesis'),
	('morpholino', 'morpholino'),
)

LOCATIONS = (
	('-20', '-20 Freezer'),
	('4', 'Small Fridge'),
	('-80', '-80 Freezer'),
	('liquid nitrogen', 'Liquid Nitrogen Tank'),
)
class ReagentInfo(models.Model):
	'''abstract base model for all reagents, will not be used in isolation, only as part of other models'''
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=25, choices=LOCATIONS, blank=True, default="-20")
	box = models.CharField(max_length=25, blank=True)
	source = models.CharField(max_length=25, blank=True)
	researcher = models.ManyToManyField(Contact, blank=True, related_name="%(class)s_related")
	vendor = models.ForeignKey(Vendor, blank=True, null=True, related_name="%(class)s_related")
	notes = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	class Meta:
		abstract=True
		ordering = ['name']
	def __unicode__(self):
		return u'%s' % self.name


class Antibody(models.Model):
	antibody = models.CharField(max_length=50)
	antibody_slug = models.SlugField(max_length=20)
	protein = models.ManyToManyField(Protein)
	protein_size = models.CharField(max_length=30, blank=True)
	source_species = models.CharField(max_length=25, choices=SPECIES)
	source = models.CharField(max_length=50, blank=True)
	catalog = models.CharField(max_length=25, blank =True)
	notes = models.TextField(max_length=250, blank=True)
	location = models.CharField(max_length=25, choices=LOCATIONS)
	vendor = models.ForeignKey(Vendor, blank=True, null=True)
	contact = models.ForeignKey(Contact, blank=True, null=True, related_name='antibody researcher')
	class Meta:
		ordering = ['antibody']
		verbose_name_plural = "Antibodies"
	def __unicode__(self):
		return u'%s' % self.antibody
	def get_absolute_url(self):
		return "/experimentdb/antibody/%i/" % self.id

class Construct(models.Model):
	construct = models.CharField(max_length=30)
	plasmid = models.CharField(max_length=30, blank=True)
	protein = models.ManyToManyField(Protein)
	source = models.CharField(max_length=20, blank=True)
	selection = models.ForeignKey('Selection')
	notes = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	reference = models.ManyToManyField(Reference, blank=True)
	contact = models.ManyToManyField(Contact, blank=True, related_name='construct researcher')
	location = models.CharField(max_length=25, choices=LOCATIONS, default="-20")
	box = models.CharField(max_length=50, blank=True)
	sequencing_contig = models.FileField(upload_to='contig/%Y/%m/%d', blank=True, help_text="LaserGene Assembled Sequencing Runs")
	sequenced_object = models.FileField(upload_to='sequenced_object/%Y/%m/%d', blank=True, help_text="LaserGene Assembled Sequence")
	class Meta:
		ordering = ['construct']
	def __unicode__(self):
		return u'%s' % self.construct
	def get_absolute_url(self):
		return "/experimentdb/construct/%i/" % self.id

class Purified_Protein(ReagentInfo):
	protein = models.ManyToManyField(Protein)
#	purification = models.ForeignKey(data_models.Experiment, blank=True, null=True)
#	result = models.ForeignKey(data_models.Result, blank=True, null=True)
	induction = models.CharField(max_length=50, blank=True, null=True)
	cells = models.CharField(max_length=20, blank=True, null=True)
#	protocol = models.ForeignKey(data_models.Protocol, blank=True, null=True)
	purification_date = models.DateField(max_length=20, blank=True, null=True)
	construct = models.ForeignKey(Construct, blank=True, null=True)
	class Meta:
		verbose_name_plural = "Purified Proteins"
	def __unicode__(self):
		return u'%s' % self.name
	@models.permalink
	def get_absolute_url(self):
		return ('purified-detail', [str(self.id)])
	class Meta:
		ordering = ['purified_protein', 'purification_date']
		verbose_name = "Purified Protein"
		
class Chemical(ReagentInfo):
	contact = models.ManyToManyField(Contact, blank=True, related_name='chemical researcher')
	def __unicode__(self):
		return u'%s' % self.name
	def get_absolute_url(self):
		return "/experimentdb/chemical/%i/" % self.name
	
class Cell(ReagentInfo):
	description = models.CharField(max_length=50, blank=True)
	species = models.CharField(max_length=50, choices=SPECIES, blank=True)
	contact = models.ManyToManyField(Contact, blank=True, related_name='cell-line researcher')
	class Meta:
		ordering = ['name']
	def __unicode__(self):
		return u'%s' % self.name
	def get_absolute_url(self):
		return "/experimentdb/cell-line/%i/" % self.id

class Primer(ReagentInfo):
	"""Model describing primer objects.
	
	These objects can be of any short nucleotide type including primers, siRNA oligos or morpholinos.  The required fields are the name and the type.  The nonrequired fields include the sequence, the protein, the ordering date and all generic reagent info fields.
	This is a subclass of the ReagentInfo abstract base class."""
	date_ordered = models.DateField(blank=True, null=True)
	primer_type = models.CharField(max_length=20, choices=PRIMER_TYPE)
	protein = models.ForeignKey(Protein, blank=True)
	sequence = models.CharField(max_length=100, blank=True)
	class Meta:
		ordering = ['primer_type']
	def __unicode__(self):
		return u'%s' % self.name
	def get_absolute_url(self):
		return "/experimentdb/primer/%i/" % self.id
		
class Selection(models.Model):
	'''model for selection of transformants'''
	selection = models.CharField(max_length=50)
	notes = models.TextField(max_length=250)
	def __unicode__(self):
		return u'%s' % self.selection
	class Meta:
	    ordering = ['selection']
		
	
class Strain(ReagentInfo):
	'''subclass of ReagentInfo abstract class'''
	background = models.ForeignKey('Strain', blank=True, null=True)
	plasmids = models.ManyToManyField(Construct, blank=True, null=True)
	selection = models.ForeignKey('Selection', blank=True, null=True)
	genotype = models.CharField(max_length=200, blank=True, help_text="BY4742 is MATa his3&Delta;1 leu2&Delta;0 lys2&Delta;0 ura3&Delta;0")
	protein = models.ManyToManyField(Protein, blank=True, null=True)
	def get_absolute_url(self):
	    return "/experimentdb/strain/%i" % self.id

