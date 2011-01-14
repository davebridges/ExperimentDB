"""This is a configuration file for the ajax lookups for the reagents app.

See http://code.google.com/p/django-ajax-selects/ for information about configuring the ajax lookups.
"""

from experimentdb.reagents.models import Antibody

from django.db.models import Q

class AntibodyLookup(object):
    """This is the generic lookup for antibodies.
	
	It is to be used for all animal requests and directs to the 'animal' channel.
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
	