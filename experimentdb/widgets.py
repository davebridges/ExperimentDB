"""This package generates custom form widgets.

See http://docs.djangoproject.com/en/1.2/ref/forms/widgets/#customizing-widget-instances for instructions to create custom widgets."""

from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import django.forms as forms

class SelectWithPop(forms.Select):
    """This widget overrides the select widget to show a popup for a foreignkey.
    
    This code is taken from http://www.hoboes.com/Mimsy/hacks/replicating-djangos-admin/"""
    def render(self, name, *args, **kwargs):
        html = super(SelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string("form/popupplus.html", {'field': name})
        return html+popupplus

	
class MultipleSelectWithPop(forms.SelectMultiple):
    """This widget overrides the select multiple widget to show a popup for a foreignkey.
    
    This code is taken from http://www.hoboes.com/Mimsy/hacks/replicating-djangos-admin/"""
    def render(self, name, *args, **kwargs):
        html = super(MultipleSelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string("form/popupplus.html", {'field': name})
        return html+popupplus
		
from django.utils.html import escape

def handlePopAdd(request, addForm, field):
	if request.method == "POST":
		form = addForm(request.POST)
		if form.is_valid():
			try:
				newObject = form.save()
			except forms.ValidationError, error:
				newObject = None
			if newObject:
				return HttpResponse('<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script>' % 	(escape(newObject._get_pk_val()), escape(newObject)))
	else:
		form = addForm()
	pageContext = {'form': form, 'field': field}
	return render_to_response("form/popadd.html", pageContext, context_instance=RequestContext(request))