from django.db import models
from experimentdb.reagents.models import Construct

INSTITUTE_TYPE = (
	('academic', 'Academic'),
	('pharmaceutical', 'Pharmaceutical'),
	)

class Institution(models.Model):
	institution = models.CharField(max_length=75)
	institution_type = models.CharField(max_length=25, choices=INSTITUTE_TYPE)
	city = models.CharField(max_length=50, blank=True)
	state = models.CharField(max_length=3, blank=True)
	country = models.CharField(max_length=30, default="United States", blank=True)
	def __unicode__(self):
		return u'%s' % self.institution

class Laboratory(models.Model):
	principal_investigator = models.CharField(max_length=25, help_text="Last Name of PI", verbose_name="Principal Investigator")
	institution = models.ForeignKey(Institution)
	department = models.CharField(max_length=50, blank=True)
	address_line_1 = models.CharField(max_length=50, blank=True)
	address_line_2 = models.CharField(max_length=50, blank=True)
	address_line_3 = models.CharField(max_length=50, blank=True)
	postal_code=models.CharField(max_length=20, blank=True)
	def __unicode__(self):
		return u'%s' % self.principal_investigator		

	
class Recipient(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	initials = models.CharField(max_length=25, blank=True)
	lab = models.ForeignKey(Laboratory)
	def __unicode__(self):
		return u'%s %s (%s lab)' %(self.first_name, self.last_name, self.lab)
		
class ConstructShipment(models.Model):
	constructs = models.ManyToManyField(Construct)
	ship_date = models.DateField()
	recieved_date = models.DateField(blank=True, null=True)
	recipient = models.ForeignKey(Recipient)
	notes = models.TextField(max_length=500)
	def __unicode__(self):
		return u'%s lab (%s)' % (self.recipient.lab, self.ship_date)
	def get_absolute_url(self):
		return '/experimentdb/shipment/%i' % self.id
	class Meta:
		ordering = ['-ship_date']

	

	