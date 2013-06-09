'''This app contains the views for the external app.

'''
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from external.models import Reference, Vendor, Contact

class PaperListView(ListView):
	'''This class generates the view for papers located at **/references/**
	
	It is subclasses for lab and interesting papers.'''

	model = Reference
	template_name = "paper-list.html"


class ReferenceCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Reference.'''
    
    model = Reference
    template_name = 'reference_form.html'
    permission_required = "external.create_reference"

class ReferenceDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Reference.'''
    
    model = Reference
    template_name = 'reference_detail.html'
    template_object_name = 'reference'

    
class ReferenceUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Reference.'''
    
    model = Reference
    template_name = 'reference_form.html'
    template_object_name = 'reference'
    permission_required = "external.update_reference"    
    
class ReferenceDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Reference.'''
    
    model = Reference
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "external.delete_reference"              
    
class ReferenceList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Reference.'''
    
    model = Reference
    template_name = 'reference_list.html'
    template_object_name = 'reference_list'       

class PaperDetailView(DetailView):
    '''This class generates the view for paper-details located at **/references/<title_slug>**.
    
    '''
    model = Reference
    slug_field = "title_slug"
    slug_url_kwarg = "title_slug"
    template_name = "paper-detail.html"
    
class VendorCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Vendor.'''
    
    model = Vendor
    template_name = 'contact_form.html'
    permission_required = "external.create_contact"

class VendorDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Vendor.'''
    
    model = Vendor
    template_name = 'contact_detail.html'
    template_object_name = 'contact'

    
class VendorUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Vendor.'''
    
    model = Vendor
    template_name = 'contact_form.html'
    template_object_name = 'contact'
    permission_required = "external.update_contact"    
    
class VendorDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Vendor.'''
    
    model = Vendor
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "external.delete_contact"              
    
class VendorList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Vendor.'''
    
    model = Vendor
    template_name = 'contact_list.html'
    template_object_name = 'contact_list'  
    
class ContactCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new Contact.'''
    
    model = Contact
    template_name = 'contact_form.html'
    permission_required = "external.create_contact"

class ContactDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing Contact.'''
    
    model = Contact
    template_name = 'contact_detail.html'
    template_object_name = 'contact'

    
class ContactUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a Contact.'''
    
    model = Contact
    template_name = 'contact_form.html'
    template_object_name = 'contact'
    permission_required = "external.update_contact"    
    
class ContactDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a Contact.'''
    
    model = Contact
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "external.delete_contact"              
    
class ContactList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of Contact.'''
    
    model = Contact
    template_name = 'contact_list.html'
    template_object_name = 'contact_list'        

