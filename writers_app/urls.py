
from django.contrib import admin
from django.urls import path, include
from .  import views
from .views import *



app_name = 'writer_app'



urlpatterns = [
    #path('', WriterListView.as_view(), name='writer_list'),
    path('create_writer/', WriterCreateView.as_view(), name='create_writer'),
    path('writer_detail/<pk>/', WriterUpdateView.as_view(), name='writer_detail'),
    # #path('create_patient/load_nurses/', views.load_nurse, name='load_nurses'),

    

   
]
