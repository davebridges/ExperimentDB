from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=25)
	middle_names = models.CharField(max_length=25, blank=True)
	last_name = models.CharField(max_length=25)
	contactID = models.SlugField(max_length=20)
	email = models.EmailField(blank=True)
	website = models.URLField(blank=True)
	address = models.TextField(max_length=500, blank=True)
	comments = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
	def get_absolute_url(self):
		return "/contact/%i/" % self.contactID

class Reference(models.Model):
	referenceID = models.SlugField(max_length=25, primary_key=True)
	SaltielLab = models.BooleanField()
	PubMedID = models.CharField(max_length=20, blank=True)
	PubMedLink = models.URLField(blank=True)
	PDFLink = models.URLField(blank=True)
	contactID = models.ManyToManyField(Contact)
	public = models.BooleanField()

	def __unicode__(self):
		return u'%s' % self.referenceID
	def get_absolute_url(self):
		return "/reference/%i/" % self.referenceID
	
class Vendor(models.Model):
	company = models.CharField(max_length = 100)
	class Meta:
		ordering = ['company',]
	def __unicode__(self):
		return u'%s' % self.company
