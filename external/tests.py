"""This package defines the tests for the external app.

It contains model tests for the models:
- Vendor
- Reference
- Contact

There are currently no views associated with these models."""

"""This file contains tests for the reagents application.

These tests include model and view tests for Strain, Primer, Cell, Antibody, Construct, Chemical, Species and Selection objects.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from external.models import Reference, Contact, Vendor, AuthorDetails


MODELS = [Contact, Vendor, Reference]

class VendorModelTests(TestCase):
    """Tests the model attributes of Vendor objects contained in the reagents app."""

    fixtures = ['test_external']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
        
    def test_create_vendor_all(self):
        """This is a test for creating a new primer object, with only the all fields being entered"""
        test_vendor = Vendor(company = "test vendor")
        test_vendor.save()
        self.assertEquals(test_vendor.__unicode__(), "test vendor")        

    def test_vendor_absolute_url(self):
        '''This tests that the absolute url for a vendor is set correctly.'''
        test_vendor = Vendor.objects.get(pk=1)
        self.assertEquals(test_vendor.get_absolute_url(), "/vendor/1/")
        
    def test_vendor_slugify(self):
        '''This tests that the vendor name is accurately converted to a slugfield upon saving.''' 
        test_vendor = Vendor(company = "test vendor")
        test_vendor.save()
        self.assertEquals(test_vendor.company_slug, "test-vendor")           

class ReferenceModelTests(TestCase):
    '''This class tests varios aspects of the `::class:Publication` model.'''
    fixtures = ['test_publication', 'test_external']

    def setUp(self):
        '''Instantiate the test client.  Creates a test user.'''
        self.client = Client()
        self.test_user = User.objects.create_user('testuser', 'blah@blah.com', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='testuser', password='testpassword')
        self.failUnless(login, 'Could not log in')
    
    def tearDown(self):
        '''Depopulate created model instances from test database.'''
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
                
    def test_create_new_paper_minimum(self):
        '''This test creates a `::class:Reference` with the required information only.'''
        test_publication = Reference(title='Test Publication.')
        test_publication.save()
        self.assertEqual(test_publication.pk, 2)
        
    #def test_create_new_paper_all(self):
        #'''This test creates a `::class:Publication` with the required information only.'''
        #test_publication = Publication(title='Test Publication') #add more fields
        #test_publication.save()        
        
    def test_paper_unicode(self):
        '''This tests the unicode representation of a `::class:Reference`.'''
        test_publication = Reference.objects.get(title_slug='14-3-3-proteins-a-number-of-functions-for-a-numbered-protein')
        self.assertEqual(test_publication.__unicode__(), "14-3-3 proteins: a number of functions for a numbered protein.")
        
    def test_paper_title_slug(self):
        '''This tests the title_slug field of a `::class:Reference`.'''
        test_publication = Reference(title='Test Publication.')
        test_publication.save()
        self.assertEqual(test_publication.title_slug, "test-publication")  
        
    def test_paper_absolute_url(self):
        '''This tests the title_slug field of a `::class:Reference`.'''
        test_publication = Reference(title='Test Publication', laboratory_paper=True)
        test_publication.save()
        self.assertEqual(test_publication.get_absolute_url(), "/reference/test-publication/") 
     
    def test_paper_doi_link(self):
        '''This tests the title_slug field of a `::class:Publication`.'''
        test_publication = Reference.objects.get(title="14-3-3 proteins: a number of functions for a numbered protein.")
        self.assertEqual(test_publication.doi_link(), "http://dx.doi.org/10.1126/stke.2962005re10") 
        
    def test_full_pmcid(self):
        '''This tests that a correct full PMCID can be generated for a `::class:Publication`.'''
        test_publication = Reference(title="Test Publication", pmcid = "12345")
        test_publication.save()
        self.assertEqual(test_publication.full_pmcid(), 'PMC12345')                         
                    
class AuthorDetailsModelTests(TestCase):
    '''This class tests varios aspects of the `::class:AuthorDetails` model.'''
    fixtures = ['test_reference', 'test_external']

    def setUp(self):
        '''Instantiate the test client.  Creates a test user.'''
        self.client = Client()
        self.test_user = User.objects.create_user('testuser', 'blah@blah.com', 'testpassword')
        self.test_user.is_superuser = True
        self.test_user.is_active = True
        self.test_user.save()
        self.assertEqual(self.test_user.is_superuser, True)
        login = self.client.login(username='testuser', password='testpassword')
        self.failUnless(login, 'Could not log in')
    
    def tearDown(self):
        '''Depopulate created model instances from test database.'''
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
                
    def test_create_new_authordetail_minimum(self):
        '''This test creates a `::class:AuthorDetails` with the required information only.'''
        test_authordetail = AuthorDetails(author=Contact.objects.get(pk=1), 
            order = 1)
        test_authordetail.save()
        
    def test_create_new_authordetail_all(self):
        '''This test creates a `::class:AuthorDetails` with the required information only.'''
        test_authordetail = AuthorDetails(author=Contact.objects.get(pk=1), 
            order = 1,
            corresponding_author = True,
            equal_contributors = True)
        test_authordetail.save()             
            
    def test_authordetail_unicode(self):
        '''This tests that the unicode representaton of an authordetail is correct.'''
        test_authordetail = AuthorDetails(author=Contact.objects.get(pk=1), 
            order = 1)
        test_authordetail.save() 
        self.assertEqual(test_authordetail.__unicode__(), 'Test User')

class ContactModelTests(TestCase):
    """Tests the model attributes of Contact objects contained in the reagents app."""

    fixtures = ['test_external']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_contact_minimal(self):
        """This is a test for creating a new primer object, with only the minimum fields being entered"""
        test_contact = Contact(first_name="Steve", last_name="TestContact")
        test_contact.save()
        self.assertEquals(test_contact.__unicode__(), "Steve TestContact")

    def test_contact_absolute_url(self):
        test_contact = Contact.objects.get(pk=1)
        self.assertEquals(test_contact.get_absolute_url(), "/contact/1/")

    def test_contact_slugify(self):
        test_contact = Contact(first_name="Steve", last_name="TestContact")
        test_contact.save()
        self.assertEquals(test_contact.__unicode__(), "Steve TestContact")
        self.assertEquals(test_contact.contactID, "steve-testcontact")  
