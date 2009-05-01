from django.db.models import Q
from django.shortcuts import render_to_response, get_object_or_404
from experimentdb.data.models import Experiment, Result, Protocol
from experimentdb.proteins.models import Protein
from experimentdb.reagents.models import Chemical, Antibody, Cell
from experimentdb.projects.models import Project, SubProject
from experimentdb.external.models import Reference, Contact
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	experiment_list = Experiment.objects.order_by('-experiment_date')
	return render_to_response('experiment_list.html', {'experiment_list': experiment_list})

@login_required
def experiment(request, experimentID):
	experiment = get_object_or_404(Experiment, pk=experimentID)
	exp_ID = experiment.experimentID
	exp_result=Result.objects.filter(experiment__experimentID=exp_ID)
	exp_protocol=Protocol.objects.filter(experiment__experimentID=exp_ID)
	exp_researcher=Contact.objects.filter(experiment__experimentID=exp_ID)
	exp_chemical=Chemical.objects.filter(experiment__experimentID=exp_ID)
	exp_antibody=Antibody.objects.filter(experiment__experimentID=exp_ID)
	exp_cell=Cell.objects.filter(experiment__experimentID=exp_ID)
	exp_protein=Protein.objects.filter(experiment__experimentID=exp_ID)
	exp_project=Project.objects.filter(experiment__experimentID=exp_ID)
	exp_subproject=SubProject.objects.filter(experiment__experimentID=exp_ID)
	return render_to_response('experiment.html', {'experiment':experiment, 'exp_result':exp_result, 'exp_protocol':exp_protocol, 'exp_researcher':exp_researcher, 'exp_chemical':exp_chemical, 'exp_cell': exp_cell,  'exp_project': exp_project, 'exp_protein': exp_protein, 'exp_subproject':exp_subproject})

@login_required
def protocol_list(request):
	protocol_list = Protocol.objects.all()
	return render_to_response('protocol_list.html', {'protocol_list':protocol_list, })

@login_required
def protocol_detail(request, protocol_slug):
	protocol = get_object_or_404(Protocol, protocol_slug=protocol_slug)
	protocol_experiments = Experiment.objects.filter(protocol=protocol)	
	return render_to_response ('protocol_detail.html', {'protocol': protocol, 'protocol_experiments':protocol_experiments})
