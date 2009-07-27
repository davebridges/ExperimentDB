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
)

PRIMER_TYPE = (
	('cloning', 'cloning'),
	('sequencing', 'sequencing'),
	('RT-PCR', 'RT-PCR'),
	('siRNA', 'siRNA'),
	('mutagenesis', 'mutagenesis'),
)

LOCATIONS = (
	('-20', '-20 Freezer'),
	('4', 'Small Fridge'),
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
	notes = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	reference = models.ManyToManyField(Reference, blank=True)
	contact = models.ManyToManyField(Contact, blank=True)
	location = models.CharField(max_length=25, choices=LOCATIONS, default="-20")
	box = models.CharField(max_length=50, blank=True)
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
	class Meta:
		verbose_name_plural = "Purified Proteins"
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
	description = models.CharField(max_length=50, blank=True)
	species = models.CharField(max_length=50, choices=SPECIES, blank=True)
	source = models.CharField(max_length=50, blank=True)
	notes = models.TextField(max_length=250, blank=True)	
	public = models.BooleanField()
	published = models.BooleanField()
	reference = models.ManyToManyField(Reference, blank=True)
	contact = models.ManyToManyField(Contact, blank=True)
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
