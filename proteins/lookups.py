"""This is a configuration file for the ajax lookups for the proteins app.

See http://code.google.com/p/django-ajax-selects/ for information about configuring the ajax lookups.
"""

from proteins.models import Protein

from django.db.models import Q
from django.utils.html import escape

from ajax_select import LookupChannel

class ProteinLookup(LookupChannel):
    """This is the generic lookup for antibodies.
	
	It is to be used for all protein requests and directs to the 'protein' channel.
	"""

    model = Protein

    def get_query(self,q,request):
        """ This sets up the query for the lookup.
		
		The lookup searches the name of the protein."""
        return Protein.objects.filter(name__icontains=q)

    def get_result(self,obj):
        """This result is the completion of what the person typed"""
        return obj.name

    def format_match(self,obj):
        """ This controls the display of the dropdown menu.
		
		This is set to show the unicode name of the protein."""
        return self.format_item_display(obj)

    def format_item_display(self,obj):
        """ the display of a currently selected object in the area below the search box. html is OK """
        return u"<div><strong>%s</strong></div>" % escape(obj.name)
