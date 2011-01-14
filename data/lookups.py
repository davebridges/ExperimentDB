"""This is a configuration file for the ajax lookups for the data app.

See http://code.google.com/p/django-ajax-selects/ for information about configuring the ajax lookups.
"""

from experimentdb.data.models import Protocol

from django.db.models import Q

class ProtocolLookup(object):
    """This is the generic lookup for protocols.
	
	It is to be used for all protocol requests and directs to the 'protocol' channel.
	"""
    def get_query(self,q,request):
        """ This sets up the query for the lookup.
		
		The lookup searches the name of the protocol."""
        return Protocol.objects.filter(protocol__icontains=q)

    def format_result(self,protocol):
        """ This controls the display of the dropdown menu.
		
		This is set to show the unicode name of the protocol."""
        return unicode(protocol)

    def format_item(self,protocol):
        """ the display of a currently selected object in the area below the search box. html is OK """
        return unicode(protocol)

    def get_objects(self,ids):
        """ given a list of ids, return the objects ordered as you would like them on the admin page.
            this is for displaying the currently selected items (in the case of a ManyToMany field)
        """
        return Protocol.objects.filter(pk__in=ids)
	