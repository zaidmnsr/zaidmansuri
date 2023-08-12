from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Create your views here.


# def index(request):
#     render(request, 'core_app/dashboard_core.html')



class CoreDashboard(TemplateView):
    template_name = "core_app/dashboard_core.html"






