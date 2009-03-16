from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from experimentdb.projects.models import Project, SubProject
from experimentdb.data.models import Experiment, Result, Protocol
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	project_list = Project.objects.order_by('-project')
	return render_to_response('projects/index.html', {'project_list': project_list})

@login_required
def detail(request, project):
	project = get_object_or_404(Project, pk=project)
	projID=project.project_slug
	proj_subproject=SubProject.objects.filter(project__project_slug=projID)
	proj_experiment=Experiment.objects.filter(project__project_slug=projID)
	return render_to_response('projects/detail.html', {'project': project, 'proj_subproject':proj_subproject, 'proj_experiment': proj_experiment})

@login_required
def subproject_detail(request, subproject):
	subproject = get_object_or_404(SubProject, pk=subproject)
	subprojID=subproject.project_slug
	proj_experiment=Experiment.objects.filter(subproject__project_slug=subprojID)
	return render_to_response('projects/detail_sub.html', {'subproject': subproject, 'proj_experiment': proj_experiment})



