'''This file controls the views for the projects app

'''

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from projects.models import Project, SubProject

class ProjectCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Project.'''
    
    model = Project
    template_name = 'project_form.html'
    permission_required = "projects.create_project"

class ProjectDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Project.'''
    
    model = Project
    template_name = 'project_detail.html'
    template_object_name = 'project'
    slug_field =  'project_slug'
    
class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Project.'''
    
    model = Project
    template_name = 'project_form.html'
    template_object_name = 'project'
    slug_field =  'project_slug'
    permission_required = "projects.update_project"    
    
class ProjectDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Project.'''
    
    model = Project
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    slug_field =  'project_slug'
    permission_required = "projects.delete_project"              
    
class ProjectList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Projects.'''
    
    model = Project
    template_name = 'project_list.html'
    template_object_name = 'project_list'    

class SubProjectCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new SubProject.'''
    
    model = SubProject
    template_name = 'project_form.html'
    permission_required = "projects.create_subproject"

class SubProjectDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing SubProject.'''
    
    model = SubProject
    template_name = 'subproject_detail.html'
    template_object_name = 'subproject'
    slug_field =  'project_slug'
    
class SubProjectUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a SubProject.'''
    
    model = SubProject
    template_name = 'subproject_form.html'
    template_object_name = 'subproject'
    slug_field =  'project_slug'
    permission_required = "projects.update_subproject"    
    
class SubProjectDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a SubProject.'''
    
    model = SubProject
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    slug_field =  'project_slug'
    permission_required = "projects.delete_subproject"              
    
class SubProjectList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of SubProjects.'''
    
    model = SubProject
    template_name = 'subproject_list.html'
    template_object_name = 'subproject_list'        