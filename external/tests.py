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

from experimentdb.external.models import Reference, Contact, Vendor


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
    
    def test_create_vendor_minimal(self):
        """This is a test for creating a new primer object, with only the minimum fields being entered"""
        test_vendor = Vendor(company = "test vendor")
        test_vendor.save()
        self.assertEquals(test_vendor.__unicode__(), "test vendor")

    def test_vendor_absolute_url(self):
        test_vendor = Vendor.objects.get(pk=1)
        self.assertEquals(test_vendor.get_absolute_url(), "/companies/1/")


class ReferenceModelTests(TestCase):
    """Tests the model attributes of Reference objects contained in the reagents app."""

    fixtures = ['test_external']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_reference_minimal(self):
        """This is a test for creating a new primer object, with only the minimum fields being entered"""
        test_reference = Reference(title = "some title")
        test_reference.save()
        self.assertEquals(test_reference.__unicode__(), "some title")

    def test_reference_absolute_url(self):
        test_reference = Reference.objects.get(pk=1)
        self.assertEquals(test_reference.get_absolute_url(), "/reference/1/")


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
