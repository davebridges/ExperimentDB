from django.db import models
from experimentdb.data.models import Sequencing, Protocol
from experimentdb.reagents.models import Primer, Construct
from experimentdb.external.models import Contact



CLONING_TYPE = (
	('PCR', 'PCR Based'),
	('digest', 'Digestion and Ligation'),
	('LIC', 'Ligation Independent Cloning'),
)

class Cloning(models.Model):
	date_completed = models.DateField(blank=True, null=True)
	construct = models.ForeignKey(Construct)
	cloning_type = models.CharField(max_length=25, choices=CLONING_TYPE)
	vector = models.CharField(max_length=25, blank=True)
	vector_CIP = models.BooleanField()
	insert = models.CharField(max_length=100, blank=True)
	primer_5prime = models.ForeignKey(Primer, blank=True, related_name='5_Primer')
	restriction_enzyme_5prime = models.CharField(max_length=7, blank=True)
	destroyed_5prime = models.BooleanField()
	primer_3prime = models.ForeignKey(Primer, blank=True, related_name='3_Primer')
	restriction_enzyme_3prime = models.CharField(max_length=7, blank=True)
	destroyed_3prime = models.BooleanField()
	ligation_temperaturee = models.IntegerField(blank=True, null=True, help_text = "in degrees Celsius")
	ligation_time = models.TimeField(blank=True, null=True)
	gel = models.ImageField(upload_to = 'cloning/%Y/%m/%d', blank=True)
	sequencing = models.ManyToManyField(Sequencing, blank=True, null=True)
	researcher = models.ManyToManyField(Contact, blank=True, null=True)
	notes = models.TextField(max_length=250, blank=True)
	def __unicode__(self):
		return u'%s ' % self.construct
	def get_absolute_url(self):
		return "/cloning/%i/" % self.id


	

class Mutagenesis(models.Model):
	construct = models.ForeignKey(Construct)
	mutation = models.CharField(max_length=25)
	date_completed = models.DateField()
	method = models.CharField(max_length=50, default = "Stratagene QuickChange")
	protocol = models.ForeignKey(Protocol, blank=True, null=True)
	sense_primer = models.ForeignKey(Primer, blank=True, related_name="sense_primer")
	antisense_primer = models.ForeignKey(Primer, blank=True, related_name="antisense_primer")
	colonies = models.IntegerField(blank=True, null=True)
	sequencing = models.ManyToManyField(Sequencing, blank=True, null=True)
	researcher = models.ManyToManyField(Contact, blank=True, null=True)
	notes = models.TextField(max_length=250, blank=True)
	def __unicode__(self):
		return u'%s ' % self.construct
	def get_absolute_url(self):
		return "/cloning/%i/" % self.id
