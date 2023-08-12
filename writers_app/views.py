from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from . models import *
from django.contrib import messages
from .forms import AddWriterForm

# Create your views here.


class WriterCreateView(CreateView):
    model = Writer
    form_class = AddWriterForm
    template_name = 'writers_app/create_writer.html'


    def form_valid(self, form):
        messages.info(self.request, 'Article created successfully')
        return super().form_valid(form)
       
    def get_success_url(self):
        return self.object.get_absolute_url()
    



class WriterUpdateView(UpdateView):
    model = Writer
    fields = '__all__'
    template_name = 'writers_app/writer_detail.html'

    def get_success_url(self):
        return self.object.get_absolute_url()
    
    def form_valid(self, form):
        messages.info(self.request, 'writer Updated successfully')
        return super().form_valid(form)