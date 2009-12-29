from django.db import models
from experimentdb.external.models import Contact, Reference

class Project(models.Model):
	project = models.CharField(max_length=50)
	project_slug = models.SlugField(max_length=15, primary_key=True)
	comments = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	collaborators = models.ManyToManyField(Contact, blank=True)
	papers = models.ManyToManyField(Reference, blank=True)
	def __unicode__(self):
		return u'%s ' % self.project
	def get_absolute_url(self):
		return "/experimentdb/project/%s" % self.project_slug

class SubProject(models.Model):
	project = models.ForeignKey(Project)
	subproject = models.CharField(max_length=50)
	project_slug = models.SlugField(max_length=15, primary_key=True)
	comments = models.TextField(max_length=250, blank=True)
	public = models.BooleanField()
	published = models.BooleanField()
	collaborators = models.ManyToManyField(Contact, blank=True)
	papers = models.ManyToManyField(Reference, blank=True)
	class Meta:
		verbose_name_plural = "Sub-Projects"
	def __unicode__(self):
		return u'%s ' % self.subproject
	def get_absolute_url(self):
		return "/experimentdb/subproject/%s/" % self.project_slug
