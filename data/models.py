from django.db import models

from experimentdb.projects.models import Project, SubProject
from experimentdb.proteins.models import Protein
from experimentdb.reagents.models import Construct, Antibody, Cell, Primer, Chemical, Strain, AnimalStrain
from experimentdb.external.models import Contact, Reference

class Protocol(models.Model):
    """Describes the protocol or protocols used to perform each experiment.  
    
    This model stores information about the protocol used for an experiment.    

    An experiment may have several protocols attached to it.  For example, one could culture and transfect cells, then generate lysates then do some western blots.
    
    Since migrating to a mediawiki based protocol storage system, the wiki_page attribute indicates the protocol wiki page.  In this model, the **protocol_revision** attribute indicates the particular revision of the protocol used for that particular experiment.  In this way a permalink can be generated to the specific protocol used for a particular experiment.  To find the protocol revision number, mouse over the permanent link on the protocol and record the number at the end of the url.
    """
       
    protocol = models.CharField(max_length=50)
    protocol_slug = models.SlugField(max_length=25)
    #reference = models.ManyToManyField(Reference, blank=True)
    protocol_file = models.FileField(upload_to='protocol', blank=True)
    protocol_revision = models.IntegerField(blank=True, null=True, help_text="ProtocolWiki page revision number")
    wiki_page = models.CharField(max_length=75, blank=True, help_text="ProtocolWiki page (via MediaWiki)")
    comments = models.TextField(max_length=500, blank=True)	
    public = models.BooleanField()
    published = models.BooleanField()
    inactive = models.BooleanField()
    def __unicode__(self):
        return u'%s ' % self.protocol
    def get_absolute_url(self):
        return "/experimentdb/protocol/%i/" % self.id
	class Meta:
		ordering = ['-protocol']


class Experiment(models.Model):
    """Experiment objects are the central objects of this database.
    
    Experiment objects contain all details about an experiment including reagents, parameters, notes, results and data."""
    project = models.ManyToManyField(Project, blank=True, null=True)
    subproject = models.ManyToManyField(SubProject, blank=True, null=True)
    experimentID = models.SlugField(max_length=50, help_text="ie DB-2008-11-11-A", primary_key=True)
    experiment = models.CharField(max_length=100)
    protocol = models.ManyToManyField(Protocol, blank=True, null=True)
    assay = models.CharField(max_length=100, blank=True, null=True)
    experiment_date = models.DateField(help_text="Date Performed")
    cellline = models.ManyToManyField(Cell, blank=True, null=True)
    antibodies = models.ManyToManyField(Antibody, blank=True, null=True)
    chemicals = models.ManyToManyField(Chemical, blank=True, null=True)
    constructs = models.ManyToManyField(Construct, blank=True, null=True)
    siRNA = models.ManyToManyField(Primer, blank=True, null=True, limit_choices_to = {'primer_type': 'siRNA'})
    strain = models.ManyToManyField(Strain, blank=True, null=True)
    animal_model = models.ManyToManyField(AnimalStrain, blank=True, null=True)
    comments = models.TextField(max_length=500, blank=True, null=True)
    researcher = models.ManyToManyField(Contact, blank=True, null=True)
    protein = models.ManyToManyField(Protein, blank=True, null=True)
    public = models.BooleanField()
    published = models.BooleanField()
    sample_storage = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        """The unicode representation of an experiment object is the experiment on assay; date."""
        return u'%s on %s; %s' % (self.experiment, self.assay, self.experiment_date)
    def get_absolute_url(self):
        """The default url for an experiment is /experimentdb/experiment/experimentID."""
        return "/experimentdb/experiment/%s/" % self.experimentID
    class Meta:
        """The default ordering for experiments is in reverse of the experiment_date."""
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
