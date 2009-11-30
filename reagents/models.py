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
	contact = models.ForeignKey(Contact, blank=True, null=True)
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
	contact = models.ManyToManyField(Contact, blank=True)
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

class Purified_Protein(models.Model):
	name = models.CharField(max_length=20, primary_key=True, help_text="ie GST-2xFYVE 2008-11-17")
	name_slug = models.SlugField(max_length=20)
	protein = models.ManyToManyField(Protein)
	purification = models.ForeignKey("data.Experiment", related_name='protein purification', blank=True, null=True)
	result = models.ForeignKey("data.Result", blank=True, null=True)
	source = models.CharField(max_length=20, blank=True)
	induction = models.CharField(max_length=50, blank=True)
	cells = models.CharField(max_length=20, blank=True)
	protocol = models.ForeignKey("data.Protocol", blank=True)
	tag = models.CharField(max_length=20, blank=True)
	construct = models.ForeignKey(Construct, blank=True)
	notes = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	reference = models.ManyToManyField(Reference, blank=True)
	researcher = models.ManyToManyField(Contact, blank=True)
	class Meta:
		verbose_name_plural = "Purified Proteins"
	def __unicode__(self):
		return u'%s' % self.name
	def get_absolute_url(self):
		return "/purfiedprotein/%s/" % self.name_slug

class Chemical(models.Model):
	chemical = models.CharField(max_length=20, primary_key=True)
	source = models.CharField(max_length=20, blank=True)
	vendor = models.ForeignKey(Vendor)
	notes = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	reference = models.ManyToManyField(Reference, blank=True)
	contact = models.ManyToManyField(Contact, blank=True)
	def __unicode__(self):
		return u'%s' % self.chemical
	def get_absolute_url(self):
		return "/project/%i/" % self.chemical
	
class Cell(models.Model):
	cellline = models.SlugField(max_length=50, primary_key=True)
	description = models.CharField(max_length=50, blank=True)
	species = models.CharField(max_length=50, choices=SPECIES, blank=True)
	source = models.CharField(max_length=50, blank=True)
	notes = models.TextField(max_length=250, blank=True)	
	public = models.BooleanField()
	published = models.BooleanField()
	reference = models.ManyToManyField(Reference, blank=True)
	contact = models.ManyToManyField(Contact, blank=True)
	class Meta:
		ordering = ['cellline']
	def __unicode__(self):
		return u'%s' % self.description
	def get_absolute_url(self):
		return "/project/%i/" % self.cellline

class Primer(models.Model):
	primer = models.CharField(max_length=30)
	date_ordered = models.DateField(blank=True)
	primer_type = models.CharField(max_length=20, choices=PRIMER_TYPE)
	vendor = models.ForeignKey(Vendor, blank=True)
	protein = models.ForeignKey(Protein, blank=True)
	sequence = models.CharField(max_length=100, blank=True)
	notes = models.TextField(max_length=250, blank=True)
	def __unicode__(self):
		return u'%s' % self.primer
	def get_absolute_url(self):
		return "/primer/%i/" % self.id
		
class Selection(models.Model):
	'''model for selection of transformants'''
	selection = models.CharField(max_length=20)
	notes = models.TextField(max_length=250)
	def __unicode__(self):
		return u'%s' % self.selection
		
class ReagentInfo(models.Model):
	'''abstract base model for all reagents, will not be used in isolation, only as part of other models'''
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=25, choices=LOCATIONS, blank=True, default="-20")
	box = models.CharField(max_length=25, blank=True)
	source = models.CharField(max_length=25, blank=True)
	researcher = models.ManyToManyField(Contact, blank=True)
	vendor = models.ForeignKey(Vendor, blank=True, null=True)
	notes = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	class Meta:
		abstract=True
		
class Strain(ReagentInfo):
	'''subclass of ReagentInfo abstract class'''
	background = models.ForeignKey('Strain', blank=True, null=True)
	plasmids = models.ForeignKey(Construct, blank=True, null=True)
	selection = models.ForeignKey('Selection', blank=True, null=True)
	

