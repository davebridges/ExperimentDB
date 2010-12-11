from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=25)
	middle_names = models.CharField(max_length=25, blank=True, null=True)
	last_name = models.CharField(max_length=25)
	contactID = models.SlugField(max_length=20, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	website = models.URLField(blank=True, null=True)
	address = models.TextField(max_length=500, blank=True, null=True)
	comments = models.TextField(max_length=250, blank=True, null=True)
	public = models.BooleanField()
	class Meta:
		ordering = ['last_name',]
	
	def __unicode__(self):
		return u'%s, %s' % (self.last_name, self.first_name)
	def get_absolute_url(self):
		return "/contact/%i/" % self.contactID

class Reference(models.Model):
	current_lab = models.BooleanField(help_text="Is this paper from our group?")
	pubMedID = models.CharField(max_length=20, blank=True, null=True)
	doiLink = models.URLField(blank=True, null=True)
	researchers = models.ManyToManyField(Contact, blank=True, null=True)
	public = models.BooleanField()

	def __unicode__(self):
		return u'%s' % self.id
	def get_absolute_url(self):
		return "/reference/%i/" % self.id
	
class Vendor(models.Model):
	company = models.CharField(max_length = 100)
	class Meta:
		ordering = ['company',]
	def __unicode__(self):
		return u'%s' % self.company
