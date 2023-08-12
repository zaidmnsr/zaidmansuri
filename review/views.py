from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from .models import *
# Create your views here.



def review(request):
    return render(request, 'review/review_list.html')




class CreateTaskView(CreateView):
    model = TaskTracker
    fields = '__all__'
    template_name = 'review/review_list.html'

    success_url = '/'