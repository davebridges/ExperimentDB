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

class LicenseViewTests(TestCase):

    def setUp(self):
        """Instantiate the test client.  Creates a test user."""
        self.client = Client()
        self.test_user = User.objects.create_user('testuser', 'blah@blah.com', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='testuser', password='testpassword')
        self.failUnless(login, 'Could not log in')

    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_license_detail(self):
        """This tests the license-detail view, ensuring that templates are loaded correctly.  

        This view uses a user with superuser permissions so does not test the permission levels for this view."""
        
        test_response = self.client.get('/license/1/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('license' in test_response.context)        
        self.assertTemplateUsed(test_response, 'license_detail.html')
        self.assertEqual(test_response.context['license'].pk, 1)
        self.assertEqual(test_response.context['license'].name, u'Fixture License')

        #verifies that a non-existent object returns a 404 error.
        null_response = self.client.get('/license/2/')
        self.assertEqual(null_response.status_code, 404)  

    def test_license_new(self):
        """This tests the license-new view, ensuring that templates are loaded correctly.  

        This view uses a user with superuser permissions so does not test the permission levels for this view."""
        
        test_response = self.client.get('/license/new/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, 'base.html')
        self.assertTemplateUsed(test_response, 'license_form.html') 

    def test_license_edit(self):
        """This tests the license-edit view, ensuring that templates are loaded correctly.  

        This view uses a user with superuser permissions so does not test the permission levels for this view."""
        
        test_response = self.client.get('/license/1/edit')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('license' in test_response.context)        
        self.assertTemplateUsed(test_response, 'license_form.html')
        self.assertEqual(test_response.context['license'].pk, 1)
        self.assertEqual(test_response.context['license'].name, u'Fixture License')

        #verifies that a non-existent object returns a 404 error.
        null_response = self.client.get('/license/2/edit')
        self.assertEqual(null_response.status_code, 404)          