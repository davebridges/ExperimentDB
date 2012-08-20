"""This is a configuration file for the ajax lookups for the reagents app.

See http://code.google.com/p/django-ajax-selects/ for information about configuring the ajax lookups.
"""

from django.db.models import Q
from django.utils.html import escape

from ajax_select import LookupChannel

from reagents.models import Antibody, Construct, Chemical, Strain, Primer, Cell

class AntibodyLookup(object):
    """This is the generic lookup for antibodies.
	
	It is to be used for all antibody requests and directs to the 'antibody' channel.
	"""
    def get_query(self,q,request):
        """ This sets up the query for the lookup.
		
		The lookup searches the name of the antibody."""
        return Antibody.objects.filter(name__icontains=q)

    def format_result(self,antibody):
        """ This controls the display of the dropdown menu.
		
		This is set to show the unicode name of the antibody, as well as the vendor and the source species."""
        #return unicode(antibody)
        return u"%s <strong>from:</strong> %s (%s)" % (antibody, antibody.vendor, antibody.source_species)


    def format_item(self,antibody):
        """ the display of a currently selected object in the area below the search box. html is OK """
        return u"%s <strong>from:</strong> %s (%s)" % (antibody, antibody.vendor, antibody.source_species)

    def get_objects(self,ids):
        """ given a list of ids, return the objects ordered as you would like them on the admin page.
            this is for displaying the currently selected items (in the case of a ManyToMany field)
        """
        return Antibody.objects.filter(pk__in=ids)
	
class ConstructLookup(object):
    """This is the generic lookup for constructs.
	
	It is to be used for all construct requests and directs to the 'construct' channel.
	"""
    def get_query(self,q,request):
        """ This sets up the query for the lookup.
		
		The lookup searches the name of the construct."""
        return Construct.objects.filter(name__icontains=q)

    def format_result(self,construct):
        """ This controls the display of the dropdown menu.
		
		This is set to show the unicode name of the construct."""
        return unicode(construct)


    def format_item(self,construct):
        """ the display of a currently selected object in the area below the search box. html is OK """
        return unicode(construct)

    def get_objects(self,ids):
        """ given a list of ids, return the objects ordered as you would like them on the admin page.
            this is for displaying the currently selected items (in the case of a ManyToMany field)
        """
        return Construct.objects.filter(pk__in=ids)
		
class ChemicalLookup(object):
    """This is the generic lookup for chemicals.
	
	It is to be used for all chemical requests and directs to the 'chemical' channel.
	"""
    def get_query(self,q,request):
        """ This sets up the query for the lookup.
		
		The lookup searches the name of the chemical."""
        return Chemical.objects.filter(name__icontains=q)

    def format_result(self,chemical):
        """ This controls the display of the dropdown menu.
		
		This is set to show the unicode name of the chemical."""
        return unicode(chemical)


    def format_item(self,chemical):
        """ the display of a currently selected object in the area below the search box. html is OK """
        return unicode(chemical)

    def get_objects(self,ids):
        """ given a list of ids, return the objects ordered as you would like them on the admin page.
            this is for displaying the currently selected items (in the case of a ManyToMany field)
        """
        return Chemical.objects.filter(pk__in=ids)	
		
class StrainLookup(object):
    """This is the generic lookup for strains.
	
	It is to be used for all strain requests and directs to the 'strain' channel.
	"""
    def get_query(self,q,request):
        """ This sets up the query for the lookup.
		
		The lookup searches the name of the strain."""
        return Strain.objects.filter(name__icontains=q)

    def format_result(self,strain):
        """ This controls the display of the dropdown menu.
		
		This is set to show the unicode name of the strain."""
        return unicode(strain)


    def format_item(self,strain):
        """ the display of a currently selected object in the area below the search box. html is OK """
        return unicode(strain)

    def get_objects(self,ids):
        """ given a list of ids, return the objects ordered as you would like them on the admin page.
            this is for displaying the currently selected items (in the case of a ManyToMany field)
        """
        return Strain.objects.filter(pk__in=ids)	

class SiRNALookup(object):
    """This is the generic lookup for siRNA.
	
	It is to be used for all siRNA requests and directs to the 'siRNA' channel
	This channel will **not** search for all Primer objects, only the ones with primer_type="siRNA".
	"""
    def get_query(self,q,request):
        """ This sets up the query for the lookup.
		
		The lookup searches the name of the siRNA."""
        return Primer.objects.filter(name__icontains=q, primer_type="siRNA")

    def format_result(self,siRNA):
        """ This controls the display of the dropdown menu.
		
		This is set to show the unicode name of the siRNA line."""
        return unicode(siRNA)


    def format_item(self,siRNA):
        """ the display of a currently selected object in the area below the search box. html is OK """
        return unicode(siRNA)

    def get_objects(self,ids):
        """ given a list of ids, return the objects ordered as you would like them on the admin page.
            this is for displaying the currently selected items (in the case of a ManyToMany field)
        """
        return Primer.objects.filter(pk__in=ids)			
		
		
class CellLineLookup(LookupChannel):

    model = Cell

    def get_query(self,q,request):
        return Cell.objects.filter(name__icontains=q)

    def get_result(self,obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.name

    def format_match(self,obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)

    def format_item_display(self,obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return u"<div><i>%s</i></div>" % escape(obj.name)