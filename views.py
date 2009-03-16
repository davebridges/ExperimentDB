from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from experimentdb.projects.models import Project, SubProject
from experimentdb.data.models import Protocol, Result, Experiment
from experimentdb.reagents.models import Antibody, Chemical, Construct, Cell
from experimentdb.proteins.models import Protein
from experimentdb.external.models import Contact, Reference

def index(request):
    return render_to_response('index.html')

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
	Q(assay__icontains=query)|
	Q(experiment__icontains=query)|
	Q(cellline__icontains=query)|
	Q(protocol__icontains=query)|
	Q(antibodies__icontains=query)|
	Q(chemicals__icontains=query)|
	Q(constructs__icontains=query)|
	Q(comments__icontains=query)|
	Q(researcher__icontains=query)|
	Q(protein__icontains=query)
        )
        results = Experiment.objects.filter(qset).distinct().order_by('-experiment_date')
    else:
        results = []
    return render_to_response("search.html", {
        "results": results,
        "query": query
    })


