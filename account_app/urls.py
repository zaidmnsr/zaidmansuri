
from django.contrib import admin
from django.urls import path, include
from . import views
from . views import *
from django.contrib.auth.views import LogoutView
from bcrm import settings




app_name = 'account_app'



urlpatterns = [
    path('login/', views.Login, name='login'),
    # path('logout/', views.Logout, name='logout'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    path('create_user/', views.CreateUser, name='create_user'),
    #path('<pk>/', ArticleUpdateView.as_view(), name='article_detail'),
    #path('create_patient/load_nurses/', views.load_nurse, name='load_nurses'),

    

   
]
