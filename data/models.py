from django.db import models
from experimentdb.projects.models import Project, SubProject
from experimentdb.proteins.models import Protein
from experimentdb.reagents.models import Antibody, Chemical, Construct, Cell, Purified_Protein, Primer
from experimentdb.external.models import Reference, Contact, Vendor

class Protocol(models.Model):
	protocol = models.CharField(max_length=50)
	protocol_slug = models.SlugField(max_length=25)
	reference = models.ManyToManyField(Reference, blank=True)
	protocol_file = models.FileField(upload_to='protocol', blank=True)
	wiki_page = models.CharField(max_length=75, blank=True)
	comments = models.TextField(max_length=500, blank=True)	
	public = models.BooleanField()
	published = models.BooleanField()
	def __unicode__(self):
		return u'%s ' % self.protocol
	def get_absolute_url(self):
		return "/protocol/%s/" % self.protocol_slug 


class Experiment(models.Model):
	project = models.ManyToManyField(Project, blank=True)
	subproject = models.ManyToManyField(SubProject, blank=True)
	experimentID = models.SlugField(max_length=50, help_text="ie DB-2008-11-11-A", primary_key=True)
	experiment = models.CharField(max_length=100)
	protocol = models.ManyToManyField(Protocol, blank=True)
	assay = models.CharField(max_length=100, blank=True)
	experiment_date = models.DateField('Date Performed')
	cellline = models.ManyToManyField(Cell, blank=True)
	antibodies = models.ManyToManyField(Antibody, blank=True)
	chemicals = models.ManyToManyField(Chemical, blank=True)
	constructs = models.ManyToManyField(Construct, blank=True)
	siRNA = models.ManyToManyField(Primer, blank=True, null=True)
	comments = models.TextField(max_length=500, blank=True)
	researcher = models.ManyToManyField(Contact, blank=True)
	protein = models.ManyToManyField(Protein, blank=True)
	purified_protein = models.ManyToManyField(Purified_Protein, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	sample_storage = models.CharField(max_length=100, blank=True)
	def __unicode__(self):
		return u'%s on %s; %s' % (self.experiment, self.assay, self.experiment_date)
	def get_absolute_url(self):
		return "/experiment/%s/" % self.experimentID
	class Meta:
		ordering = ['-experiment_date']

class Result(models.Model):
	experiment = models.ForeignKey(Experiment)
	conclusions = models.TextField(max_length=500, blank=True)
	#datafile = models.MultiFileField(upload_to='raw/%Y/%m/%d', blank=True)	
	file1 = models.FileField(upload_to='raw/%Y/%m/%d', blank=True)
	file2 = models.FileField(upload_to='raw/%Y/%m/%d', blank=True)
	file3 = models.FileField(upload_to='raw/%Y/%m/%d', blank=True)
	rawscan1 = models.ImageField(upload_to='raw/%Y/%m/%d', blank=True)
	rawscan2 = models.ImageField(upload_to='raw/%Y/%m/%d', blank=True)
	rawscan3 = models.ImageField(upload_to='raw/%Y/%m/%d', blank=True)
	rawscan4 = models.ImageField(upload_to='raw/%Y/%m/%d', blank=True)
	rawscan5 = models.ImageField(upload_to='raw/%Y/%m/%d', blank=True)
	result_figure1 = models.ImageField(upload_to='final/%Y/%m/%d', blank=True)
	result_figure2 = models.ImageField(upload_to='final/%Y/%m/%d', blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	def __unicode__(self):
		return u'%s ' % self.experiment
	def get_absolute_url(self):
		return "/result/%i/" % self.id


class Sequencing(models.Model):
	clone_name = models.CharField(max_length=15)
	construct = models.ForeignKey(Construct)
	primer = models.ForeignKey(Primer)
	file = models.FileField(upload_to='sequencing/%Y/%m/%d', blank=True)
	sequence = models.CharField(max_length=1500)
	correct = models.BooleanField()
	notes = models.TextField(max_length=250,blank=True)
	date = models.DateField(blank=True)
	sample_number = models.IntegerField(max_length=8, blank=True, null=True)
	gel_number = models.IntegerField(max_length=8, blank=True, null=True)
	lane_number = models.IntegerField(max_length=3, blank=True, null=True)
	def __unicode__(self):
		return u'%s-%s' % (self.construct,self.clone_name)
