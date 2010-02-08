from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from experimentdb.projects.models import Project, SubProject
from experimentdb.data.models import Experiment, Result, Protocol
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def index(request):
	project_list = Project.objects.order_by('-project')
	return render_to_response('project_index.html', {'project_list': project_list},context_instance=RequestContext(request))

@login_required
def detail(request, project):
	project = get_object_or_404(Project, pk=project)
	return render_to_response('project_detail.html', {'project': project},context_instance=RequestContext(request))

@login_required
def subproject_detail(request, subproject):
	subproject = get_object_or_404(SubProject, pk=subproject)
	return render_to_response('project_detail_sub.html', {'subproject': subproject},context_instance=RequestContext(request))



