"""This package contains the model information for the external app.

It defines the structure and behavior of the following models:
- Contact
- Vendor
- Reference

"""
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models

class Contact(models.Model):
    """This model defines a contact.

    This is intended to be a person who is involved in the research program, and may be but it not necessarily a database user.
    The required fields are first_name and last_name.
    """
    first_name = models.CharField(max_length=25)
    middle_names = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25)
    user = models.ForeignKey(User, blank=True, null=True, help_text="Select from the list if the contact is also a database user")
    contactID = models.SlugField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    comments = models.TextField(max_length=250, blank=True, null=True)
    public = models.BooleanField()
    class Meta:
        ordering = ['last_name',]
	
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
   
    @models.permalink
    def get_absolute_url(self):
        return ('contact-detail', [str(self.id)])

    def save(self):
        """The save is over-ridden to slugify the contact field into a slugfield named contactID."""
        self.contactID = slugify( self.__unicode__() )
        super( Contact, self ).save()

class Reference(models.Model):
    """This model contains objects of the class reference.

    It is intended to keep track of specific papers that pertain to protocols, experiments or projects.

    The only required field for this model is a title."""
    title = models.CharField(max_length=255, help_text="This can be a preliminary manuscript, just ensure that public is not checked")
    current_lab = models.BooleanField(help_text="Is this paper from our group?")
    pubMedID = models.CharField(max_length=20, blank=True, null=True)
    doiLink = models.URLField(blank=True, null=True)
    researchers = models.ManyToManyField(Contact, blank=True, null=True)
    public = models.BooleanField()

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('reference-detail', [str(self.id)])
	
class Vendor(models.Model):
    """This model contains objects of the class vendor.

    It is intended to be used to indicate companies from which reagents are obtained.
    The only required field is company."""
    company = models.CharField(max_length = 100)
    company_slug = models.SlugField(max_length = 100, help_text="Will be set automatically upon saving")
    class Meta:
	ordering = ['company',]

    def __unicode__(self):
        return u'%s' % self.company

    @models.permalink
    def get_absolute_url(self):
        return ('vendor-detail', [str(self.id)])

    def save(self):
        """The save is over-ridden to slugify the contact field into a slugfield named contactID."""
        self.company_slug = slugify( self.__unicode__() )
        super( Vendor, self ).save()
