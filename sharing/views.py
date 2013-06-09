'''This package controls the views generated for the sharing app'''


from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from sharing.models import ConstructShipment

class ConstructShipmentCreate(PermissionRequiredMixin, CreateView):
    '''This view is for creating a new ConstructShipment.'''
    
    model = ConstructShipment
    template_name = 'construct_shipment_form.html'
    permission_required = "sharing.create_constructshipment"

class ConstructShipmentDetail(LoginRequiredMixin, DetailView):
    '''This view is for viewing ConstructShipment.'''
    
    model = ConstructShipment
    template_name = 'construct_shipment_detail.html'
    template_object_name = 'construct_shipment'

    
class ConstructShipmentUpdate(PermissionRequiredMixin, UpdateView):
    '''This view is for editing a ConstructShipment.'''
    
    model = ConstructShipment
    template_name = 'construct-shipment_form.html'
    template_object_name = 'construct_shipment'
    permission_required = "sharing.update_constructshipment"    
    
class ConstructShipmentDelete(PermissionRequiredMixin, DeleteView):
    '''This view is for deleting a ConstructShipment.'''
    
    model = ConstructShipment
    template_name = 'confirm_delete.html'
    template_object_name = 'object'
    permission_required = "sharing.delete_construct_shipment"              
    
class ConstructShipmentList(LoginRequiredMixin, ListView):
    '''This view is for viewing a list of ConstructShipment.'''
    
    model = ConstructShipment
    template_name = 'construct_shipment_list.html'
    template_object_name = 'construct-shipment_list' 
