from django.contrib import admin
from django.urls import path
from . views import *

app_name = 'core_app'

urlpatterns = [
    path('', CoreDashboard.as_view(), name='core_dashboard'), 
    
    
]
