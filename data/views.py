"""This module provides the views for working with the data package.
This module will generate index and detail views for experiments and protocols as well as for the form to enter new results through an experiment.  Several other generic views are found in data.urls.
"""

from django.db.models import Q
from django.shortcuts import render_to_response, get_object_or_404
from experimentdb.data.models import Experiment, Result, Protocol
from experimentdb.data.forms import ResultForm, ResultFormSet, ExperimentForm
from experimentdb.proteins.models import Protein
from experimentdb.reagents.models import Chemical, Antibody, Cell
from experimentdb.projects.models import Project, SubProject
from experimentdb.external.models import Reference, Contact
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
from django.http import HttpResponseRedirect


@login_required
def index(request):
	"""This view shows a list of all experiments.

	This list is ordered by the experiment date in descending order.  This view could potentially be rendered by a generic view.
	"""
	experiment_list = Experiment.objects.order_by('-experiment_date')
	return render_to_response('experiment_list.html', {'experiment_list': experiment_list},context_instance=RequestContext(request))

@login_required
def experiment(request, experimentID):
	"""This renders a detailed page of an experiment.

	The view will show the experiment, and all associated reagents, proteins, projects and results associated with this object.
	"""
	experiment = get_object_or_404(Experiment, pk=experimentID)
	return render_to_response('experiment.html', {'experiment':experiment}, context_instance=RequestContext(request))

@login_required
def protocol_list(request):
	"""This renders a view in which all protocols are displayed.

	In the case of deprecated protocols (i.e. protocols not marked as active), these are not shown.  This view could also be rendered as a generic view.
	"""
	protocol_list = Protocol.objects.all()
	return render_to_response('protocol_list.html', {'protocol_list':protocol_list, },context_instance=RequestContext(request))

@login_required
def protocol_detail(request, protocol_slug):
	"""This renders a view in which a protocol detail page is shown.

	This view should be deprecated in favor of a redirection directly to the wiki page for this protocol
	"""
	protocol = get_object_or_404(Protocol, protocol_slug=protocol_slug)
	protocol_experiments = Experiment.objects.filter(protocol=protocol)	
	return render_to_response ('protocol_detail.html', {'protocol': protocol, 'protocol_experiments':protocol_experiments},context_instance=RequestContext(request))

@login_required
def result_new(request, experimentID):
	"""This renders a form to add a new result.

	This view will be sent from a particular experiment and will attach the result to that particular experiment.	
	"""
	experiment = get_object_or_404(Experiment, pk=experimentID)
	if request.method == "POST":
		form = ResultForm(request.POST, request.FILES)
		if form.is_valid():
			result = form.save(commit=False)
			result.experiment_id = experiment.experimentID
			result.save()
			form.save()
			return HttpResponseRedirect( experiment.get_absolute_url() )
	else:
		form = ResultForm()
	return render_to_response('result_form.html', {'form':form, 'experiment':experiment},context_instance=RequestContext(request))
	
@permission_required('data.change_experiment')
def experiment_edit(request, experimentID):
    """Renders a form to edit an experiment and associated formsets for experimental results.
	
    Takes a request in the form of experiment/(experimentID)/edit and returns the experiment_result_form.html form."""
    experiment = get_object_or_404(Experiment, pk=experimentID)
    if request.method == "POST":
        form = ExperimentForm(request.POST)
        if form.is_valid():
            experiment = form.save(commit=False)
            formset = ResultFormSet(request.POST, instance=experiment)
            if result_formset.is_valid():
                experiment.save()
                result_formset.save()                
            return HttpResponseRedirect( experiment.get_absolute_url() )
    else:
        form = ExperimentForm()
        formset = ResultFormSet(instance=Experiment())
    return render_to_response("experiment_result_form.html", {"form": form,"formset": formset,}, context_instance=RequestContext(request))
