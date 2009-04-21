from django.db import models
from experimentdb.proteins.models import Protein
from experimentdb.external.models import Contact, Reference, Vendor
#from experimentdb.cloning.models import Cloning

ANTIBODY_SPECIES = (
	('rabbit', 'rabbit'),
	('mouse', 'mouse'),
	('goat', 'goat')
)

PRIMER_TYPE = (
	('cloning', 'cloning'),
	('sequencing', 'sequencing'),
	('RT-PCR', 'RT-PCR'),
	('siRNA', 'siRNA'),
	('mutagenesis', 'mutagenesis'),
)


class Antibody(models.Model):
	antibody = models.CharField(max_length=50)
	antibody_slug = models.SlugField(max_length=20)
	protein = models.ManyToManyField(Protein)
	protein_size = models.CharField(max_length=30, blank=True)
	source_species = models.CharField(max_length=25, choices=ANTIBODY_SPECIES)
	source = models.CharField(max_length=50, blank=True)
	catalog = models.CharField(max_length=25, blank =True)
	notes = models.TextField(max_length=250, blank=True)	
	def __unicode__(self):
		return u'%s' % self.antibody
	def get_absolute_url(self):
		return "/antibody/%i/" % self.antibody_slug

class Construct(models.Model):
	construct = models.CharField(max_length=30)
	plasmid = models.CharField(max_length=30, blank=True)
	protein = models.ManyToManyField(Protein)
#	cloning = models.ForeignKey(Cloning)
	source = models.CharField(max_length=20, blank=True)
	resistance = models.CharField(max_length=20, default="Ampicillin")
	notes = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	reference = models.ManyToManyField(Reference, blank=True)
	contact = models.ManyToManyField(Contact, blank=True)
	def __unicode__(self):
		return u'%s' % self.construct
	def get_absolute_url(self):
		return "/construct/%i/" % self.id

class Purified_Protein(models.Model):
	name = models.CharField(max_length=20, primary_key=True, help_text="ie GST-2xFYVE 2008-11-17")
	name_slug = models.SlugField(max_length=20)
	protein = models.ManyToManyField(Protein)
	purification = models.ForeignKey("data.Experiment", related_name='protein purification')
	result = models.ForeignKey("data.Result")
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
	def __unicode__(self):
		return u'%s' % self.name
	def get_absolute_url(self):
		return "/purfieiedprotein/%s/" % self.name_slug

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
	source = models.CharField(max_length=50, blank=True)
	notes = models.TextField(max_length=250, blank=True)	
	public = models.BooleanField()
	published = models.BooleanField()
	reference = models.ManyToManyField(Reference, blank=True)
	contact = models.ManyToManyField(Contact, blank=True)
	def __unicode__(self):
		return u'%s' % self.cellline
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
