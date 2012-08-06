"""This package describes the schema for the projects app.

The two models are for projects and subprojects, with the latter having a foreignkey to the former."""

from django.db import models
from django.template.defaultfilters import slugify

class Project(models.Model):
    """This defines the major project model.

    Projects are thought of as large, grant sized groups of data, whereas subprojects are paper sized projects, attached to a main project."""
    project = models.CharField(max_length=50)
    project_slug = models.SlugField(max_length=15, blank=True, null=True, editable=False) #this field is slugified on save
    comments = models.TextField(max_length=250, blank=True, null=True)
    public = models.BooleanField()
    published = models.BooleanField()
    collaborators = models.ManyToManyField('external.Contact', blank=True, null=True)
    papers = models.ManyToManyField('external.Reference', blank=True, null=True)

    def __unicode__(self):
        return u'%s ' % self.project

    @models.permalink
    def get_absolute_url(self):
        '''The absolute url of a project is /project/slug as defined by project-detail.'''
        return ('project-detail', [str(self.project_slug)])

    def save(self, *args, **kwargs):
        '''The save method is over-ridden to generate the slugified project field.'''
        if not self.id:
            self.project_slug = slugify(self.project)
        super(Project, self).save(*args, **kwargs)



class SubProject(models.Model):
    """This model defines a subproject.

    These projects are generally offshoots of major projectsand are paper or thesis sized projects."""
    project = models.ForeignKey('Project')
    subproject = models.CharField(max_length=50)
    project_slug = models.SlugField(max_length=15, blank=True, null=True, editable=False) #this field is slugified on save
    comments = models.TextField(max_length=250, blank=True, null=True)
    public = models.BooleanField()
    published = models.BooleanField()
    collaborators = models.ManyToManyField('external.Contact', blank=True, null=True)
    papers = models.ManyToManyField('external.Reference', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sub-Projects"
        verbose_name = "Sub-Project"

    def __unicode__(self):
        return u'%s ' % self.subproject

    @models.permalink
    def get_absolute_url(self):
        return ('subproject-detail', [str(self.project_slug)])

    def save(self, *args, **kwargs):
        '''The save method is over-ridden to generate the slugified subproject field.'''
        if not self.id:
            self.project_slug = slugify(self.subproject)
        super(SubProject, self).save(*args, **kwargs)
