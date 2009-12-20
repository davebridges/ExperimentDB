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
    """This model stores details about the generation of new recombinant DNA molecules.

    """

    date_completed = models.DateField(blank=True, null=True)
    construct = models.ForeignKey(Construct, help_text="Result of Cloning Project", related_name="final_clone")
    cloning_type = models.CharField(max_length=25, choices=CLONING_TYPE)
    vector = models.ForeignKey(Construct, blank=True, null=True, related_name="recipient_vector")
    vector_CIP = models.BooleanField()
    insert = models.CharField(max_length=100, blank=True)
    primer_5prime = models.ForeignKey(Primer, blank=True, related_name='5_Primer', verbose_name="5' PCR Primer")
    restriction_enzyme_5prime = models.CharField(max_length=7, blank=True, verbose_name="insert 5' site")
    vector_restriction_enzyme_5prime = models.CharField(max_length=7, blank=True, verbose_name="vector 5' site")
    destroyed_5prime = models.BooleanField(verbose_name="is the 5' site destroyed?")
    primer_3prime = models.ForeignKey(Primer, blank=True, related_name='3_Primer', verbose_name="3' PCR Primer")
    restriction_enzyme_3prime = models.CharField(max_length=7, blank=True, verbose_name="vector 3' site")
    vector_restriction_enzyme_3prime = models.CharField(max_length=7, blank=True, verbose_name="vector 3' site")
    destroyed_3prime = models.BooleanField(verbose_name="is the 3' site destroyed?")
    ligation_temperaturee = models.IntegerField(blank=True, null=True, help_text = "in degrees Celsius")
    ligation_time = models.TimeField(blank=True, null=True)
    gel = models.ImageField(upload_to = 'cloning/%Y/%m/%d', blank=True)
    sequencing = models.ManyToManyField(Sequencing, blank=True, null=True)
    researcher = models.ManyToManyField(Contact, blank=True, null=True)
    notes = models.TextField(max_length=250, blank=True)
    def __unicode__(self):
        return u'%s ' % self.construct
    def get_absolute_url(self):
        return "experimentdb/clones/cloning/%i/" % self.id


	

class Mutagenesis(models.Model):
    """This model contains data describing the generation of muationns in clones"""
    construct = models.ForeignKey(Construct, related_name="mutant")
    mutation = models.CharField(max_length=25)
    template = models.ForeignKey(Construct, related_name="template")
    date_completed = models.DateField()
    method = models.CharField(max_length=50, default = "Stratagene QuickChange")
    protocol = models.ForeignKey(Protocol, blank=True, null=True)
    sense_primer = models.ForeignKey(Primer, blank=True, null=True, related_name="sense_primer")
    antisense_primer = models.ForeignKey(Primer, blank=True, null=True, related_name="antisense_primer")
    colonies = models.IntegerField(blank=True, null=True)
    sequencing = models.ManyToManyField(Sequencing, blank=True, null=True)
    researcher = models.ManyToManyField(Contact, blank=True, null=True)
    notes = models.TextField(max_length=250, blank=True)
    class Meta:
        verbose_name_plural = "Mutageneses"
    def __unicode__(self):
        return u'%s ' % self.construct
    def get_absolute_url(self):
        return "experimentdb/clones/mutagenesis/%i/" % self.id
