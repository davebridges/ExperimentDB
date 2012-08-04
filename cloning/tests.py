"""This file contains tests for the cloning application.

These tests include model and view tests for Cloning and Mutagenesis objects.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from cloning.models import Cloning, Mutagenesis
from reagents.models import Construct, Primer
from data.models import Sequencing
from external.models import Contact

MODELS = [Cloning, Mutagenesis]

class CloningModelTests(TestCase):
    """Tests the model attributes of Cloning objects contained in the reagents app."""

    fixtures = ['test_construct','test_primer', 'test_external', 'test_sequencing']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_cloning_minimal(self):
        """This is a test for creating a new Cloning object, with only the minimum fields being entered."""
        test_cloning = Cloning(construct = Construct.objects.get(pk=1), 
        	cloning_type="PCR")
        test_cloning.save()
        self.assertEquals(test_cloning.__unicode__(), "Fixture Construct cloning")
        
    def test_cloning_full(self):
        """This is a test for creating a full Cloning object, with all fields being entered, with the exception of gel."""
        test_cloning = Cloning(construct = Construct.objects.get(pk=1), 
        	cloning_type="PCR",
        	date_completed = '2012-01-01',
        	vector = Construct.objects.get(pk=1),
        	vector_CIP = True,
        	insert = 'Rab5 ORF',
        	primer_5prime = Primer.objects.get(pk=1),
        	primer_3prime = Primer.objects.get(pk=1),
        	restriction_enzyme_5prime = "EcoRI",
        	restriction_enzyme_3prime = "BamHI",
        	vector_restriction_enzyme_5prime = "EcoRI",
        	vector_restriction_enzyme_3prime = "BamHI",
        	destroyed_5prime = True,
        	destroyed_3prime = False,
        	ligation_temperature = 15,
        	ligation_time = '18:00',
        	notes = "Some Notes")
        test_cloning.save()
        test_cloning.researcher.add(Contact.objects.get(pk=1))
        test_cloning.sequencing.add(Sequencing.objects.get(pk=1))
        self.assertEquals(test_cloning.__unicode__(), "Fixture Construct cloning")            

    def test_cloning_absolute_url(self):
        """This is a test for creating a new Cloning object, and checking the url generated."""
        test_cloning = Cloning(construct = Construct.objects.get(pk=1), 
        	cloning_type="PCR")
        test_cloning.save()
        self.assertEquals(test_cloning.get_absolute_url(), "/cloning/cloning/1/")

