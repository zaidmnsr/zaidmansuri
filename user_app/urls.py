
from django.contrib import admin
from django.urls import path, include
from .  import views
from .views import *



app_name = 'user_app'



urlpatterns = [
    path('login/', views.Login, name='login'),
    path('create_user/', views.CreateUser, name='create_user'),
    #path('<pk>/', ArticleUpdateView.as_view(), name='article_detail'),
    #path('create_patient/load_nurses/', views.load_nurse, name='load_nurses'),

    

   
]
