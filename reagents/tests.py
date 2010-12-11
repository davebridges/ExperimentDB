"""This file contains tests for the reagents application.

These tests include model and view tests for Strain, Primer, Cell, Antibody, Construct, Chemical, Species and Selection objects.
"""

import datetime

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from experimentdb.reagents.models import Primer, Cell, Antibody, Construct, Chemical, Species, Selection
from experimentdb.external.models import Reference, Contact, Vendor


MODELS = [Primer, Cell, Antibody, Construct, Chemical, Species, Selection]

class PrimerModelTests(TestCase):
    """Tests the model attributes of Primer objects contained in the reagents app."""

    fixtures = ['test_external']
    
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
             researcher = Contact.objects.get(pk=1),
             vendor = Vendor.objects.get(pk=1),
             notes = "some notes on the object",
             reference = Reference.objects.get(pk=1),
             public = True,
             published = True)
        test_primer.save()
        self.assertEquals(test_primer.__unicode__(), "test primer")
