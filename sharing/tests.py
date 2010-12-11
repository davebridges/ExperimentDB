"""This file contains tests for the sharing application.

These tests include model and view tests for the following models:
- Institution
- Laboratory
- Recipient
- ConstructShipment
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from experimentdb.sharing.models import Institution, Laboratory, Recipient, ConstructShipment
from experimentdb.reagents.models import Construct
from experimentdb.external.models import Contact

MODELS = [Institution, Laboratory, Recipient, ConstructShipment]

class ConstructShipmentModelTests(TestCase):
    """Tests the model attributes of ConstructShipment objects contained in the reagents app."""

    fixtures = ['test_construct','test_recipient', 'test_laboratory']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_construct_shipment_minimal(self):
        """This is a test for creating a new construct shipment, with only the minimum fields being entered"""
        test_shipment = ConstructShipment(ship_date = "2010-01-01", recipient = Recipient.objects.get(pk=1))
        test_shipment.save()
        test_shipment.constructs.add(Construct.objects.get(pk=1))
        self.assertEquals(test_shipment.__unicode__(), "Fixture Laboratory (2010-01-01)")

    def test_create_construct_shipment_all_fields(self):
        """This is a test for creating a new construct shipment object, with all fields being entered"""
        test_shipment = ConstructShipment(
            ship_date = "2010-01-01", 
            recieved_date = "2010-02-01",
            recipient = Recipient.objects.get(pk=1),
            notes = "here are some notes on the shipment")
        test_shipment.save()
        test_shipment.constructs.add(Construct.objects.get(pk=1))
        self.assertEquals(test_shipment.__unicode__(), "Fixture Laboratory (2010-01-01)")


class RecipientModelTests(TestCase):
    """Tests the model attributes of Recipient objects contained in the reagents app."""

    fixtures = ['test_laboratory',]
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_recipient_minimal(self):
        """This is a test for creating a new recipient, with only the minimum fields being entered"""
        test_recipient = Recipient(
            first_name = "Test",
            last_name = "Recipient",
            lab = Laboratory.objects.get(pk=1))
        test_recipient.save()
        self.assertEquals(test_recipient.__unicode__(), "Test Recipient (Fixture Laboratory)")

    def test_create_recipient_all_fields(self):
        """This is a test for creating a new recipient, with all fields being entered"""
        test_recipient = Recipient(
            first_name = "Test",
            last_name = "Recipient",
            initials = "E.",
            lab = Laboratory.objects.get(pk=1))
        test_recipient.save()
        self.assertEquals(test_recipient.__unicode__(), "Test Recipient (Fixture Laboratory)")

class LaboratoryModelTests(TestCase):
    """Tests the model attributes of Laboratory objects contained in the reagents app."""

    fixtures = ['test_institution','test_external']
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_laboratory_minimal(self):
        """This is a test for creating a new laboratory, with only the minimum fields being entered"""
        test_laboratory = Laboratory(
            principal_investigator = "Testing",
            institution = Institution.objects.get(pk=1))
        test_laboratory.save()
        self.assertEquals(test_laboratory.__unicode__(), "Testing Laboratory")

    def test_create_laboratory_all_fields(self):
        """This is a test for creating a new recipient object, with all fields being entered"""
        test_laboratory = Laboratory(
            principal_investigator = "Testing",
            contact = Contact.objects.get(pk=1),
            department = "Department of Test Research",
            address_line_1 = "Room 1111",
            address_line_2 = "Test Research Center",
            address_line_3 = "1111 Test Road",
            postal_code = "11111",
            institution = Institution.objects.get(pk=1))
        test_laboratory.save()
        self.assertEquals(test_laboratory.__unicode__(), "Testing Laboratory")

class InstitutionModelTests(TestCase):
    """Tests the model attributes of Laboratory objects contained in the reagents app."""

    fixtures = []
    
    def setUp(self):
        """Instantiate the test client."""
        self.client = Client()
    
    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    
    def test_create_institution_minimal(self):
        """This is a test for creating a new institution, with only the minimum fields being entered"""
        test_institution = Institution(institution="Testing Institution")
        test_institution.save()
        self.assertEquals(test_institution.__unicode__(), "Testing Institution")

    def test_create_institution_all_fields(self):
        """This is a test for creating a new institution object, with all fields being entered"""
        test_institution = Institution(
            institution="Testing Institution",
            institution_type = "academic",
            city = "Test City",
            state = "Test State",
            country = "CA")
        test_institution.save()
        self.assertEquals(test_institution.__unicode__(), "Testing Institution")

