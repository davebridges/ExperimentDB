"""This file contains tests for the hypotheses application.

These tests include model tests for Hypothesis objects.
"""
import datetime

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from hypotheses.models import Hypothesis, Manipulation, Effect, Process, Context, Evidence
from proteins.models import Protein
from reagents.models import Chemical

MODELS = [Hypothesis, Manipulation, Effect, Process, Context, Evidence]

class HypothesisModelTests(TestCase):
    """Tests the model attributes of Hypothesis objects contained in the hypotheses app."""

    fixtures = ['test_manipulation','test_protein', 'test_process', 'test_entity', 'test_context', 'test_evidence', 'test_hypothesis', 'initial_data']
    
    def setUp(self):
        """Instantiate the test client.  Creates a test user."""
        self.client = Client()
        self.test_user = User.objects.create_user('blah', 'blah@blah.com', 'blah')
        self.test_user.is_superuser = True
        self.test_user.save()
        self.client.login(username='blah', password='blah')

    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_create_hypothesis_minimal(self):
        """This is a test for creating a new Hypothesis object, with only the minimum fields being entered.  It also tests the unicode representation."""
        test_hypothesis = Hypothesis(
		    manipulation = Manipulation.objects.get(pk=1), 
			effect = Effect.objects.get(pk=1),
			process = Process.objects.get(pk=1)
			)
        test_hypothesis.save()
        self.assertEquals(test_hypothesis.__unicode__(), "Fixture Protein Overexpression positively regulates glucose import")
		
    def test_create_hypothesis_all_fields_process(self):
        """This is a test for creating a new Hypothesis object, with all fields being entered.  There is one test for process and one for entity (since both cannot be entered simultaneously).  It also tests the unicode representation."""
        test_hypothesis = Hypothesis(
		    manipulation = Manipulation.objects.get(pk=1), 
			effect = Effect.objects.get(pk=1),
			process = Process.objects.get(pk=1),
			context = Context.objects.get(pk=1),
			)
        test_hypothesis.save()
        test_evidence = Evidence.objects.get(pk=1)
        test_hypothesis.evidence.add(test_evidence) # tests the addition of evidence as a m2m field
        test_hypothesis.identical_hypotheses.add(test_hypothesis)	# tests the addition of a symmetrical hypothesis as a m2m field
        self.assertEquals(test_hypothesis.__unicode__(), 'Fixture Protein Overexpression positively regulates glucose import in Fixture Context')

def test_create_hypothesis_all_fields_entity(self):		
        """This is a test for creating a new Hypothesis object, with all fields being entered.  There is one test for process and one for entity (since both cannot be entered simultaneously).  It also tests the unicode representation."""
	
        test_hypothesis = Hypothesis(
		    manipulation = Manipulation.objects.get(pk=1), 
			effect = Effect.objects.get(pk=1),
			process = Process.objects.get(pk=1),
			context = Context.objects.get(pk=1),
			evidence = Evidence.objects.get(pk=1),
			)
        test_hypothesis.save()
        test_evidence = Evidence.objects.get(pk=1)
        test_hypothesis.evidence.add(test_evidence) # tests the addition of evidence as a m2m field
        test_hypothesis.identical_hypotheses.add(test_hypothesis)	# tests the addition of a symmetrical hypothesis as a m2m field		
        self.assertEquals(test_hypothesis.__unicode__(), 'Fixture Protein Overexpression positively regulates glucose import in Fixture Context')			
		
def test_create_hypothesis_create_date(self):
        """This is a test for checking that the create and modified date are being set correctly."""
        test_hypothesis = Hypothesis(
		    manipulation = Manipulation.objects.get(pk=1), 
			effect = Effect.objects.get(pk=1),
			process = Process.objects.get(pk=1)
			)
        test_hypothesis.save()
        self.assertEquals(test_hypothesis.__unicode__(), "Fixture Protein Overexpression positively regulates glucose import")
        self.assertEquals(test_hypothesis.create_date, datetime.date.today())		
        self.assertEquals(test_hypothesis.modified_date, datetime.date.today())			
				
class ManipulationModelTests(TestCase):
    """Tests the model attributes of Manipulation objects contained in the hypotheses app."""

    fixtures = ['test_protein','test_chemical']
    
    def setUp(self):
        """Instantiate the test client.  Creates a test user."""
        self.client = Client()
        self.test_user = User.objects.create_user('blah', 'blah@blah.com', 'blah')
        self.test_user.is_superuser = True
        self.test_user.save()
        self.client.login(username='blah', password='blah')

    def tearDown(self):
        """Depopulate created model instances from test database."""
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_create_manipulation_minimal_treatment_protein_added(self):
        """This is a test for creating a new Manipulation object, with only the minimum fields being entered.  It also tests the unicode representation.  This tests for adding a protein."""
        test_manipulation = Manipulation(
		    type = "Treatment",
			protein_added = Protein.objects.get(pk=1)
			)
        test_manipulation.save()
        self.assertEquals(test_manipulation.__unicode__(), "Fixture Protein Treatment")

    def test_create_manipulation_minimal_treatment_chemical(self):
        """This is a test for creating a new Manipulation object, with only the minimum fields being entered.  It also tests the unicode representation.  This tests for chemcial treatment."""
        test_manipulation = Manipulation(
		    type = "Treatment",
			chemical = Chemical.objects.get(pk=1)
			)
        test_manipulation.save()
        self.assertEquals(test_manipulation.__unicode__(), "Test Chemical Treatment")

    def test_create_manipulation_minimal_overexpression(self):
        """This is a test for creating a new Manipulation object, with only the minimum fields being entered.  It also tests the unicode representation.  This tests for protein overexpression."""
        test_manipulation = Manipulation(
		    type = "Overexpression",
			protein = Protein.objects.get(pk=1)
			)
        test_manipulation.save()
        self.assertEquals(test_manipulation.__unicode__(), "Fixture Protein Overexpression")

    def test_create_manipulation_minimal_knockdown(self):
        """This is a test for creating a new Manipulation object, with only the minimum fields being entered.  It also tests the unicode representation.  This tests for protein knockdown."""
        test_manipulation = Manipulation(
		    type = "Knockdown",
			protein = Protein.objects.get(pk=1)
			)
        test_manipulation.save()
        self.assertEquals(test_manipulation.__unicode__(), "Fixture Protein Knockdown")	

    def test_create_manipulation_minimal_knockout(self):
        """This is a test for creating a new Manipulation object, with only the minimum fields being entered.  It also tests the unicode representation.  This tests for knockout."""
        test_manipulation = Manipulation(
		    type = "Knockout",
			protein = Protein.objects.get(pk=1)
			)
        test_manipulation.save()
        self.assertEquals(test_manipulation.__unicode__(), "Fixture Protein Knockout")		

class EvidenceViewTests(TestCase):
    '''This class tests the views for :class:`~hypotheses.models.Evidence` objects.'''

    fixtures = ['test_evidence',]

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

    def test_evidence_new(self):
        """This tests the evidence-new view, ensuring that templates are loaded correctly.  

        This view uses a user with superuser permissions so does not test the permission levels for this view."""
        
        test_response = self.client.get('/hypotheses/evidence/new/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTemplateUsed(test_response, 'base.html')
        self.assertTemplateUsed(test_response, 'evidence_form.html') 

    def test_evidence_edit(self):
        """This tests the evidence-edit view, ensuring that templates are loaded correctly.  

        This view uses a user with superuser permissions so does not test the permission levels for this view."""
        
        test_response = self.client.get('/hypotheses/evidence/1/edit/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('evidence' in test_response.context)        
        self.assertTemplateUsed(test_response, 'evidence_form.html')
        self.assertEqual(test_response.context['evidence'].pk, 1)
        self.assertEqual(test_response.context['evidence'].name, u'Fixture Evidence')

        #verifies that a non-existent object returns a 404 error.
        null_response = self.client.get('/hypotheses/evidence/2/edit/')
        self.assertEqual(null_response.status_code, 404)   

    def test_evidence_delete(self):
        """This tests the evidence-delete view, ensuring that templates are loaded correctly.  

        This view uses a user with superuser permissions so does not test the permission levels for this view."""
        
        test_response = self.client.get('/hypotheses/evidence/1/delete/')
        self.assertEqual(test_response.status_code, 200)
        self.assertTrue('evidence' in test_response.context)        
        self.assertTemplateUsed(test_response, 'confirm_delete.html')
        self.assertEqual(test_response.context['evidence'].pk, 1)
        self.assertEqual(test_response.context['evidence'].name, u'Fixture Evidence')

        #verifies that a non-existent object returns a 404 error.
        null_response = self.client.get('/hypotheses/evidence/2/delete/')
        self.assertEqual(null_response.status_code, 404)         