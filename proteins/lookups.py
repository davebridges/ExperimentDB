"""This is a configuration file for the ajax lookups for the proteins app.

See http://code.google.com/p/django-ajax-selects/ for information about configuring the ajax lookups.
"""

from experimentdb.proteins.models import Protein

from django.db.models import Q

class ProteinLookup(object):
    """This is the generic lookup for antibodies.
	
	It is to be used for all protein requests and directs to the 'protein' channel.
	"""
    def get_query(self,q,request):
        """ This sets up the query for the lookup.
		
		The lookup searches the name of the protein."""
        return Protein.objects.filter(name__icontains=q)

    def format_result(self,protein):
        """ This controls the display of the dropdown menu.
		
		This is set to show the unicode name of the protein."""
        return unicode(protein)

    def format_item(self,protein):
        """ the display of a currently selected object in the area below the search box. html is OK """
        return unicode(protein)

    def get_objects(self,ids):
        """ given a list of ids, return the objects ordered as you would like them on the admin page.
            this is for displaying the currently selected items (in the case of a ManyToMany field)
        """
        return Protein.objects.filter(pk__in=ids)
	