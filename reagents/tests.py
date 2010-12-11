"""This file contains tests for the reagents application.

These tests include model and view tests for Strain, Primer, Cell, Antibody, Construct, Chemical, Species and Selection objects.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from experimentdb.reagents.models import Primer, Cell, Antibody, Construct, Chemical, Strain, Species, Selection
from experimentdb.external.models import Reference, Contact, Vendor
from experimentdb.proteins.models import Protein


MODELS = [Primer, Cell, Antibody, Construct, Chemical, Species, Selection]

class PrimerModelTests(TestCase):
    """Tests the model attributes of Primer objects contained in the reagents app."""

    fixtures = ['test_external','test_protein']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_primer_minimal(self):
        """This is a test for creating a new primer object, with only the minimum fields being entered"""
        test_primer = Primer(name = "test primer", primer_type="cloning")
        test_primer.save()
        self.assertEquals(test_primer.__unicode__(), "test primer")

    def test_primer_slugify(self):
        """This is a test for the primer name being correctly slugified"""
        test_primer = Primer(name = "test primer", primer_type="cloning")
        test_primer.save()
        self.assertEquals(test_primer.slug, "test-primer")

    def test_create_primer_all_fields(self):
        """This is a test for creating a new primer object, with only the all fields being entered"""
        test_primer = Primer(
             name = "test primer", 
             primer_type="cloning",
             date_ordered = "2010-01-01",
             sequence = "ATGGCTTCTT",
             location = "-20",
             box = "sample box",
             source = "that guy",
             vendor = Vendor.objects.get(pk=1),
             notes = "some notes on the object",
             public = True,
             published = True)
        test_primer.save()
        test_primer.researcher.add(Contact.objects.get(pk=1))
        test_primer.protein.add(Protein.objects.get(pk=1))
        test_primer.reference.add(Reference.objects.get(pk=1))
        self.assertEquals(test_primer.__unicode__(), "test primer")

class AntibodyModelTests(TestCase):
    """Tests the model attributes of Antibody objects contained in the reagents app."""

    fixtures = ['test_external', 'test_species', 'test_protein']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_antibody_minimal(self):
        """This is a test for creating a new antibody object, with only the minimum fields being entered"""
        test_antibody = Antibody(name = "test antibody", source_species = "rabbit")
        test_antibody.save()
        self.assertEquals(test_antibody.__unicode__(), "test antibody")

    def test_antibody_slugify(self):
        """This is a test for the antibody name being correctly slugified"""
        test_antibody = Antibody(name = "test antibody", source_species = "rabbit")
        test_antibody.save()
        self.assertEquals(test_antibody.slug, "test-antibody")

    def test_create_antibody_all_fields(self):
        """This is a test for creating a new antibody object, with only the all fields being entered"""
        test_antibody = Antibody(
             name = "test antibody", 
             protein_size = "120 kDa",
             source_species = "rabbit",
             species = Species.objects.get(pk=1),
             catalog = "abc1234",
             location = "-20",
             box = "sample box",
             source = "that guy",
             vendor = Vendor.objects.get(pk=1),
             notes = "some notes on the object",
             public = True,
             published = True)
        test_antibody.save()
        test_antibody.researcher.add(Contact.objects.get(pk=1))
        test_antibody.protein.add(Protein.objects.get(pk=1))
        test_antibody.reference.add(Reference.objects.get(pk=1))
        self.assertEquals(test_antibody.__unicode__(), "test antibody")

class ConstructModelTests(TestCase):
    """Tests the model attributes of Construct objects contained in the reagents app."""

    fixtures = ['test_external','test_protein', 'test_selection']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_cell_line_minimal(self):
        """This is a test for creating a new construct object, with only the minimum fields being entered"""
        test_construct = Construct(name = "test construct")
        test_construct.save()
        self.assertEquals(test_construct.__unicode__(), "test construct")

    def test_construct_slugify(self):
        """This is a test for the construct name being correctly slugified"""
        test_construct = Construct(name = "test construct")
        test_construct.save()
        self.assertEquals(test_construct.slug, "test-construct")

    def test_create_construct_all_fields(self):
        """This is a test for creating a new construct object, with only the all fields being entered"""
        test_construct = Construct(
             name = "test construct", 
             plasmid = "test plasmid",
             selection = Selection.objects.get(pk=1),
             location = "-20",
             box = "sample box",
             source = "that guy",
             vendor = Vendor.objects.get(pk=1),
             notes = "some notes on the object",
             public = True,
             published = True)
        test_construct.save()
        test_construct.researcher.add(Contact.objects.get(pk=1))
        test_construct.protein.add(Protein.objects.get(pk=1))
        test_construct.reference.add(Reference.objects.get(pk=1))
        self.assertEquals(test_construct.__unicode__(), "test construct")

class CellModelTests(TestCase):
    """Tests the model attributes of Cell objects contained in the reagents app."""

    fixtures = ['test_external','test_protein', 'test_species']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_cell_line_minimal(self):
        """This is a test for creating a new cell line object, with only the minimum fields being entered"""
        test_cell_line = Cell(name = "test cell line")
        test_cell_line.save()
        self.assertEquals(test_cell_line.__unicode__(), "test cell line")

    def test_cell_line_slugify(self):
        """This is a test for the cell line name being correctly slugified"""
        test_cell_line = Cell(name = "test cell line")
        test_cell_line.save()
        self.assertEquals(test_cell_line.slug, "test-cell-line")

    def test_create_cell_line_all_fields(self):
        """This is a test for creating a new cell_line object, with only the all fields being entered"""
        test_cell_line = Cell(
             name = "test cell_line", 
             description = "test cell line description",
             species = "rabbit",
             cell_line_species = Species.objects.get(pk=1),
             location = "-20",
             box = "sample box",
             source = "that guy",
             vendor = Vendor.objects.get(pk=1),
             notes = "some notes on the object",
             public = True,
             published = True)
        test_cell_line.save()
        test_cell_line.researcher.add(Contact.objects.get(pk=1))
        test_cell_line.protein.add(Protein.objects.get(pk=1))
        test_cell_line.reference.add(Reference.objects.get(pk=1))
        self.assertEquals(test_cell_line.__unicode__(), "test cell_line")

class ChemicalModelTests(TestCase):
    """Tests the model attributes of Chemical objects contained in the reagents app."""

    fixtures = ['test_external','test_protein']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_chemical_minimal(self):
        """This is a test for creating a new chemical object, with only the minimum fields being entered"""
        test_chemical = Chemical(name = "test chemical")
        test_chemical.save()
        self.assertEquals(test_chemical.__unicode__(), "test chemical")

    def test_chemical_slugify(self):
        """This is a test for the cell line name being correctly slugified"""
        test_chemical = Chemical(name = "test chemical")
        test_chemical.save()
        self.assertEquals(test_chemical.slug, "test-chemical")

    def test_create_chemical_all_fields(self):
        """This is a test for creating a new chemical object, with only the all fields being entered"""
        test_chemical = Chemical(
             name = "test chemical", 
             cas = "53123-88-9",
             location = "-20",
             box = "sample box",
             source = "that guy",
             vendor = Vendor.objects.get(pk=1),
             notes = "some notes on the object",
             public = True,
             published = True)
        test_chemical.save()
        test_chemical.researcher.add(Contact.objects.get(pk=1))
        test_chemical.protein.add(Protein.objects.get(pk=1))
        test_chemical.reference.add(Reference.objects.get(pk=1))
        self.assertEquals(test_chemical.__unicode__(), "test chemical")

class StrainModelTests(TestCase):
    """Tests the model attributes of Strain objects contained in the reagents app."""

    fixtures = ['test_external','test_protein', 'test_selection', 'test_strain', 'test_construct', 'test_species']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_strain_minimal(self):
        """This is a test for creating a new strain object, with only the minimum fields being entered"""
        test_strain = Strain(name = "test strain")
        test_strain.save()
        self.assertEquals(test_strain.__unicode__(), "test strain")

    def test_strain_slugify(self):
        """This is a test for the cell line name being correctly slugified"""
        test_strain = Strain(name = "test strain")
        test_strain.save()
        self.assertEquals(test_strain.slug, "test-strain")

    def test_create_strain_all_fields(self):
        """This is a test for creating a new strain object, with only the all fields being entered"""
        test_strain = Strain(
            name = "test strain", 
            background = Strain.objects.get(pk=1),
            selection = Selection.objects.get(pk=1),
            species = "rabbit",
            strain_species = Species.objects.get(pk=1),
            genotype = "MATa his3&Delta;1 leu2&Delta;0 lys2&Delta;0 ura3&Delta;0",
            location = "-20",
            box = "sample box",
            source = "that guy",
            vendor = Vendor.objects.get(pk=1),
            notes = "some notes on the object",
            public = True,
            published = True)
        test_strain.save()
        test_strain.researcher.add(Contact.objects.get(pk=1))
        test_strain.plasmids.add(Construct.objects.get(pk=1))
        test_strain.protein.add(Protein.objects.get(pk=1))
        test_strain.reference.add(Reference.objects.get(pk=1))
        self.assertEquals(test_strain.__unicode__(), "test strain")

class SpeciesModelTests(TestCase):
    """Tests the model attributes of Species objects contained in the reagents app."""

    fixtures = []
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_species_minimal(self):
        """This is a test for creating a new species object, with only the minimum fields being entered"""
        test_species = Species(common_name = "test species")
        test_species.save()
        self.assertEquals(test_species.__unicode__(), "test species")

    def test_species_slugify(self):
        """This is a test for the cell line name being correctly slugified"""
        test_species = Species(common_name = "test species")
        test_species.save()
        self.assertEquals(test_species.species_slug, "test-species")

    def test_create_species_all_fields(self):
        """This is a test for creating a new species object, with only the all fields being entered"""
        test_species = Species(
            common_name = "test species", 
            taxonomy_id = "4932")
        test_species.save()
        self.assertEquals(test_species.__unicode__(), "test species")

class SelectionModelTests(TestCase):
    """Tests the model attributes of Selection objects contained in the reagents app."""

    fixtures = []
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_selection_minimal(self):
        """This is a test for creating a new selection object, with only the minimum fields being entered"""
        test_selection = Selection(selection = "test selection")
        test_selection.save()
        self.assertEquals(test_selection.__unicode__(), "test selection")

    def test_selection_slugify(self):
        """This is a test for the cell line name being correctly slugified"""
        test_selection = Selection(selection = "test selection")
        test_selection.save()
        self.assertEquals(test_selection.slug, "test-selection")

    def test_create_selection_all_fields(self):
        """This is a test for creating a new selection object, with only the all fields being entered"""
        test_selection = Selection(
            selection = "test selection", 
            notes = "4932")
        test_selection.save()
        self.assertEquals(test_selection.__unicode__(), "test selection")
