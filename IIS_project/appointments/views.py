from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from appointments import models
from .filters import AppointmentFilter
#from appointments.forms import AppointmentForm

# Create your views here.

class AppointmentList(FilterView):
    #model = models.Appointment
    filterset_class = AppointmentFilter
    template_name = 'appointments/appointments_list.html'


class AppointmentCreateView(CreateView):
    model = models.Appointment
    template_name = 'appointments/appointments_form.html'
    fields = ['appointment_date', 'appointment_time', 'patient']


class AppointmentDetailView(DetailView):
    context_object_name = 'appointment'
    model = models.Appointment
    template_name = 'appointments/appointments_detail.html'


class AppointmentUpdateView(UpdateView):
    model = models.Appointment
    template_name = 'appointments/appointments_form.html'
    fields = ['appointment_date', 'appointment_time', 'patient']
    #form_class = AppointmentForm


class AppointmentDeleteView(DeleteView):
    model = models.Appointment
    template_name = 'appointments/appointments_delete.html'
    success_url = reverse_lazy('appointments:appointments_list')
