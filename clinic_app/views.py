from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView
from . models import *
from .forms import *
from django.urls import reverse

# Create your views here.


class PatientCreateView(CreateView):
    model = Patient
    #fields = '__all__'
    form_class = CreatePatientForm
    template_name = 'clinic_app/create_patient.html'

    def get(self, request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs)

    
    # def patient_create_view(request):
    #   form = CreatePatientForm()
    #   if request.method == 'POST':
    #       form = CreatePatientForm(request.POST)
    #       if form.is_valid():
    #           form.save(commit=False)
    #           Patient.looked_by_nurse = form.cleaned_data['form.nurse.field.value']
    #           form.save(commit=True)
    #           return redirect('create_patient')
    #   return render(request, 'clinic_app/create_patient.html', {'form': form})
    
    def get_success_url(self):
        return self.object.get_absolute_url()

    
    
# def load_nurse(request):
#         provider_id = request.GET.get("provider")
#         id_looked_by_nurse = Nurse.objects.filter(works_for_provider=provider_id)
#         return render(request, "clinic_app/nurses_options.html", {"id_looked_by_nurse": id_looked_by_nurse})