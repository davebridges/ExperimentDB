from django.db import models
from experimentdb.reagents.models import Construct
from experimentdb.experimentdata.models import *



CLONING_TYPE = (
	('PCR', 'PCR Based'),
	('digest', 'Digestion and Ligation'),
	('LIC', 'Ligation Independent Cloning'),
)

class Cloning(models.Model):
	date_completed = models.DateField(blank=True, null=True)
	cloning_type = models.CharField(max_length=25, choices=CLONING_TYPE)
	vector = models.ForeignKey('Construct')
	vector_CIP = models.BooleanField()
	insert = models.CharField(max_length=100, blank=True)
	primer_5prime = models.ForeignKey('Primer', blank=True)
	restriction_enzyme_5prime = models.CharField(max_length=7, blank=True)
	destroyed_5prime = models.BooleanField()
	primer_3prime = models.ForeignKey('Primer', blank=True)
	restriction_enzyme_3prime = models.CharField(max_length=7, blank=True)
	destroyed_3prime = models.BooleanField()
	ligation_temperaturee = models.IntegerField(blank=True, null=True, help_text = "in degrees Celsius")
	ligation_time = models.TimeField(blank=True, null=True)
	gel = models.ImageField(upload_to = 'cloning/%Y/%m/%d', blank=True)
	sequencing = models.ManyToManyField('Sequencing', blank=True, null=True)
	notes = models.TextField(max_length=250, blank=True)
	
