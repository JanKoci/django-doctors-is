from django.shortcuts import render
from visitations import models
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from patients.models import Patient
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def VisitationsView(request, patient):
    object_list = models.Visitation.objects.all().filter(patient=patient)
    context_dict = {'object_list' : object_list, 'patient' : patient}
    return render(request, 'visitations/visitation_list.html', context=context_dict)


class VisitationCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Visitation
    template_name = 'visitations/visitation_form.html'
    fields = ['appointment_date', 'appointment_time', 'patient', 'note']

    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = Patient.objects.get(pk=self.kwargs['patient'])
        return initial


class VisitationDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Visitation
    template_name = 'visitations/visitation.html'


class VisitationUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Visitation
    template_name = 'visitations/visitation_form.html'
    fields = ['appointment_date', 'appointment_time', 'patient', 'note']


class VisitationDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    model = models.Visitation
    template_name = 'visitations/visitation_confirm_delete.html'

    def get_success_url(self):
        visitation = models.Visitation.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy("visitations:visitation_list", kwargs={'patient':visitation.patient.pk})
