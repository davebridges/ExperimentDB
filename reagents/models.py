from django.db import models
from experimentdb.proteins.models import Protein
from experimentdb.external.models import Contact, Reference, Vendor


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
		return "/antibody/%i/" % self.antibody_slug

class Construct(models.Model):
	construct = models.CharField(max_length=30)
	plasmid = models.CharField(max_length=30, blank=True)
	protein = models.ManyToManyField(Protein)
	source = models.CharField(max_length=20, blank=True)
	resistance = models.CharField(max_length=20, default="Ampicillin")
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
	protein = models.CharField(max_length=20, primary_key=True, help_text="ie GST-2xFYVE 2008-11-17")
	name_slug = models.SlugField(max_length=20)
	protein = models.ManyToManyField(Protein)
	purification = models.ForeignKey("data.Experiment", related_name='protein purification', blank=True, null=True)
	result = models.ForeignKey("data.Result", blank=True, null=True)
	source_old = models.CharField(max_length=20, blank=True)
	induction = models.CharField(max_length=50, blank=True)
	cells = models.CharField(max_length=20, blank=True)
	protocol = models.ForeignKey("data.Protocol", blank=True)
	tag = models.CharField(max_length=20, blank=True)
	construct = models.ForeignKey(Construct, blank=True)
	class Meta:
		verbose_name_plural = "Purified Proteins"
	def __unicode__(self):
		return u'%s' % self.name
	def get_absolute_url(self):
		return "/experimentdb/purfiedprotein/%s/" % self.name_slug

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
		return "/experimentdb/cell-line/%i/" % self.name

class Primer(ReagentInfo):
	date_ordered = models.DateField(blank=True)
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
	selection = models.CharField(max_length=20)
	notes = models.TextField(max_length=250)
	def __unicode__(self):
		return u'%s' % self.selection
		
	
class Strain(ReagentInfo):
	'''subclass of ReagentInfo abstract class'''
	background = models.ForeignKey('Strain', blank=True, null=True)
	plasmids = models.ManyToManyField(Construct, blank=True, null=True)
	selection = models.ForeignKey('Selection', blank=True, null=True)
	genotype = models.CharField(max_length=200, blank=True, help_text="BY4742 is MATa his3&Delta;1 leu2&Delta;0 lys2&Delta;0 ura3&Delta;0")
	protein = models.ManyToManyField(Protein, blank=True, null=True)
	def get_absolute_url(self):
	    return "/experimentdb/strain/%i" % self.id

