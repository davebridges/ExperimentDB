"""This package describes the models in the reagents app.

The models are :class:`~experimentdb.models.ReagentInfo`, which is an abstract superclass of:
* :class:`~experimentdb.models.Primer`
* :class:`~experimentdb.models.Cell`
* :class:`~experimentdb.models.Antibody`
* :class:`~experimentdb.models.Strain`
* :class:`~experimentdb.models.AnimalStrain`
* :class:`~experimentdb.models.Chemical`
* :class:`~experimentdb.models.Construct`

There are also separate models for :class:`~experimentdb.models.License`, :class:`~experimentdb.models.Species` and :class:`~experimentdb.models.Selection` which are supplementary to these models.

The :class:`~experimentdb.models.ReagentInfo class provides generic fields to all the models, while each subclass provides extra specific fields.
"""

from django.db import models
from django.template.defaultfilters import slugify

from experimentdb.proteins.models import Protein
from experimentdb.external.models import Contact, Reference, Vendor




SPECIES = (
	('rabbit', 'rabbit'),
	('mouse', 'mouse'),
	('human', 'human'),
	('monkey', 'monkey'),
	('goat', 'goat'),
	('sheep', 'sheep'),
	('rat', 'rat'),
	('fly', 'fly'),
	('brewers yeast', 'brewers yeast'),
)

PRIMER_TYPE = (
	('cloning', 'cloning'),
	('sequencing', 'sequencing'),
	('RT-PCR', 'RT-PCR'),
	('siRNA', 'siRNA'),
	('genotyping', 'Genotyping'),
	('dsRNA', 'dsRNA Amplification'),
	('mutagenesis', 'mutagenesis'),
	('morpholino', 'morpholino'),
)

LOCATIONS = (
	('-20', '-20 Freezer'),
	('4', 'Small Fridge'),
	('-80', '-80 Freezer'),
	('liquid nitrogen', 'Liquid Nitrogen Tank'),
)


class ReagentInfo(models.Model):
    '''Abstract base model for all reagents, will not be used in isolation, only as part of other models.

    This superclass provides several generic fields, available to all reagents.  The only required field of all reagents is name.
    It orders all reagents by name, although this may be over-ridden in the model.  
    It also sets sets their __unicode__ representation to be "name".'''
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=25, choices=LOCATIONS, blank=True, null=True, default="-20")
    box = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(max_length=25, blank=True, null=True)
    researcher = models.ManyToManyField(Contact, blank=True, null=True, related_name="%(class)s_researcher")
    vendor = models.ForeignKey(Vendor, blank=True, null=True, related_name="%(class)s_vendor")
    protein = models.ManyToManyField(Protein, null=True, blank=True)
    license = models.ForeignKey('License', null=True, blank=True, help_text="Terms of Use")
    notes = models.TextField(max_length=250, blank=True, null=True)
    reference = models.ManyToManyField(Reference, blank=True, null=True)
    public = models.BooleanField()
    published = models.BooleanField()

    class Meta:
        abstract=True
        ordering = ['name']

    def __unicode__(self):
        return u'%s' % self.name

class Antibody(ReagentInfo):
    """This model describes antibodies.

    The required fields are name and source_species.
    This model is a subclass of ReagentInfo.
    """
    protein_size = models.CharField(max_length=30, blank=True, null=True)
    source_species = models.CharField(max_length=25, choices=SPECIES, help_text="The species in which the antibody was raised in, i.e. which secondary antibody to use")
    species = models.ForeignKey('Species', blank=True, null=True, help_text="The species in which the antibody was raised in, i.e. which secondary antibody to use")
    catalog = models.CharField(max_length=25, blank =True, null=True)
    dilution = models.IntegerField(blank=True, null=True, help_text="What fold dilution is appropriate for this antibody")

    class Meta:
        verbose_name_plural = "Antibodies"

    @models.permalink
    def get_absolute_url(self):
        return ("antibody-detail", [str(self.id)])

    def save(self):
        """The save is over-ridden to slugify the name field into a slugfield."""
        self.slug = slugify( self.name )
        super( Antibody, self ).save()

class Construct(ReagentInfo):
    """This model describes recombinant DNA objects.

    The only required field is name.
    It is a subclass of ReagentInfo.
    """
    plasmid = models.CharField(max_length=30, blank=True, null=True)
    selection = models.ForeignKey('Selection', blank=True, null=True)
    sequencing_contig = models.FileField(upload_to='contig/%Y/%m/%d', blank=True, null=True, help_text="LaserGene Assembled Sequencing Runs")
    sequenced_object = models.FileField(upload_to='sequenced_object/%Y/%m/%d', blank=True, null=True, help_text="LaserGene Assembled Sequence")

    def save(self):
        """The save is over-ridden to slugify the name field into a slugfield."""
        self.slug = slugify( self.name )
        super( Construct, self ).save()

    @models.permalink
    def get_absolute_url(self):
        return ("construct-detail", [str(self.id)])
	

class Chemical(ReagentInfo):
    """This model describes objects of the class Chemical.

    It is intended to describe chemicals used in experiments.
    The only required field is name.
    This model is a subclass of ReagentInfo."""
    cas = models.CharField(max_length=12, 
        verbose_name="Chemical Abstract Service Number",
        blank=True,
        null=True)
    cid = models.CharField(max_length=12, 
        verbose_name="PubChem Chemical Identification", 
        blank=True, 
        null=True)    

    def save(self):
        """The save is over-ridden to slugify the name field into a slugfield."""
        self.slug = slugify( self.name )
        super( Chemical, self ).save()

    @models.permalink
    def get_absolute_url(self):
        return ("chemical-detail", [str(self.id)])

	
class Cell(ReagentInfo):
    """This model describes objects of the class Cell.

    This model is intended to be used to store information about mammalian cell lines.
    The only required field is name.
    This model is a subclass of ReagentInfo."""
    description = models.CharField(max_length=50, blank=True, null=True)
    species = models.CharField(max_length=50, choices=SPECIES, blank=True, null=True)
    cell_line_species = models.ForeignKey('Species', blank=True, null=True)
    uri = models.URLField(blank=True, null=True, help_text="A URI for a cell line.  Search http://bioportal.bioontology.org/search and find an instance of the Cell Line Ontology for a particular cell line")	
    
    class Meta:
        ordering = ['name']
        verbose_name = "Cell Line"
        verbose_name_plural = "Cell Lines"

    @models.permalink
    def get_absolute_url(self):
        return ("cell-detail", [str(self.id)])

    def save(self):
        """The save is over-ridden to slugify the name field into a slugfield."""
        self.slug = slugify( self.name )
        super( Cell, self ).save()


class Primer(ReagentInfo):
    """Model describing primer objects.
	
    These objects can be of any short nucleotide type including primers, siRNA oligos or morpholinos.  
    The required fields are the name and the type.  
    The nonrequired fields include the sequence, the protein, the ordering date and all generic reagent info fields.
    This is a subclass of the ReagentInfo abstract base class.
    """
    date_ordered = models.DateField(blank=True, null=True)
    primer_type = models.CharField(max_length=20, choices=PRIMER_TYPE)
    sequence = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['primer_type']

    @models.permalink
    def get_absolute_url(self):
        return ('primer-detail', [str(self.id)])

    def save(self):
        """The save is over-ridden to slugify the name field into a slugfield."""
        self.slug = slugify( self.name )
        super( Primer, self ).save()

		
class Selection(models.Model):
    '''Model for selection conditions of transformants.

    This object has one required field, being **selection**.  An optional comments field is also available.

    Initial data upon installation includes resistance to ampicillin or kanamycin.  Other selective markers should be added at /experimentdb/selection/new
    '''
    selection = models.CharField(max_length=50)
    selection_slug = models.SlugField(max_length=50)
    notes = models.TextField(max_length=250, blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('selection-detail', [str(self.id)])

    class Meta:
        ordering = ['selection']

    def __unicode__(self):
        return '%s' % self.selection

    def save(self):
        """The save is over-ridden to slugify the selection field into a slugfield."""
        self.slug = slugify( self.selection )
        super( Selection, self ).save()
		
	
class Strain(ReagentInfo):
    '''Model describing biological strains.

    This was devised to organize yeast strains, but can be used for bacteria or other organisms as well.
    The only required field is **name**.
    This is a subclass of ReagentInfo abstract class
    '''
    background = models.ForeignKey('Strain', blank=True, null=True)
    plasmids = models.ManyToManyField('Construct', blank=True, null=True)
    selection = models.ForeignKey('Selection', blank=True, null=True)
    species = models.CharField(max_length=50, choices=SPECIES, blank=True, null=True, default='brewers yeast')
    strain_species = models.ForeignKey('Species', blank=True, null=True)
    genotype = models.CharField(max_length=200, blank=True, help_text="BY4742 is MATa his3&Delta;1 leu2&Delta;0 lys2&Delta;0 ura3&Delta;0")
    
    def save(self):
        """The save is over-ridden to slugify the name field into a slugfield."""
        self.slug = slugify( self.name )
        super( Strain, self ).save()

    @models.permalink
    def get_absolute_url(self):
        return ("strain-detail", [str(self.id)])
        
class AnimalStrain(ReagentInfo):
    '''Model describing animal strains.

    This contains only basic information about an animal model.  For more details enter a URI in the url field for this strain.
    This is a subclass of ReagentInfo abstract class
    '''
    background = models.CharField(max_length=100, blank=True, null=True)
    strain_species = models.ForeignKey('Species', blank=True, null=True)
    url = models.URLField(verify_exists=False, blank=True, null=True, help_text="Link to a URI the strain, for example from Jackson Labs or another online database")
    
    def save(self):
        """The save is over-ridden to slugify the name field into a slugfield."""
        self.slug = slugify( self.name )
        super( AnimalStrain, self ).save()

    @models.permalink
    def get_absolute_url(self):
        """The absolute url of this is the animal-detail page with the id number."""    
        return ("animal-detail", [str(self.id)])        

class Species(models.Model):
    '''Model for indicating specific species.  
       
    The only required field is common_name.
    This is used with Strain, Cell and Antibody objects.
    Currently the species field, with the old choices=SPECIES is present until data can be migrated.  
    Upon installation, initial data is provided for rabbit, mouse, human, yeast and goat species.  
    More species can be added at /experimentdb/species/new.
    '''
    common_name = models.CharField(max_length=50, help_text="Generic name of the species")
    species_slug = models.SlugField(max_length=50, help_text="Will be automatically generated upon saving.")
    taxonomy_id = models.IntegerField(blank=True, null=True, help_text="NCBI taxonomy id, find at http://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/")

    def __unicode__(self):
        return u'%s' %self.common_name

    def save(self):
        """The save is over-ridden to slugify the common_name field into a slugfield."""
        self.species_slug = slugify( self.common_name )
        super( Species, self ).save()

    @models.permalink
    def get_absolute_url(self):
        return ('species-detail', [str(self.id)])
        
class License(models.Model):
    """These object define terms of use for reagents.
    
    License is an optional field for all reagent objects.  The only required field is name.
    There are optional fields for notes (for pasting the entire agreement), url, and (as yes/no/unknown fields) for acknowledgements, distribution or sharing, use on human subjects, using them for commercialization purposes directly or through target modifications.
    These details are commonly filled out in material transfer agreements."""
    
    name = models.CharField(max_length=50)
    notes = models.TextField(max_length=1000, blank=True, null=True, help_text="Paste the entire license")
    url = models.URLField(verify_exists=True, blank=True, null=True, help_text="Link to a web copy of the license")
    acknowledgement = models.NullBooleanField(help_text="For use in publications, must the source be acknowledged?")
    distributable = models.NullBooleanField(help_text="Can this reagent be distributed?")
    human_subjects = models.NullBooleanField(help_text="Can this reagents be used on human subjects?")
    commericalization = models.NullBooleanField(help_text="Can this reagent be used for commercialization purposes?")
    modification = models.NullBooleanField(help_text="Can this reagent be modified?")
    modification_license = models.NullBooleanField(help_text="Must the modified reagent conform to this license?")

    def __unicode__(self):
        """The unicode representation of a :class:`~experimentdb.models.License` object is its name."""
        return u'%s' %self.name

    @models.permalink
    def get_absolute_url(self):
        """The url of a :class:`~experimentdb.models.License` object is **/licence/#**"""
        return ('license-detail', [str(self.id)])    

