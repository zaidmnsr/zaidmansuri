"""
URL configuration for bcrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . views import *
from .  import views


app_name = 'website_app'


urlpatterns = [
    path('websites/', views.getAllWebsites, name='getAllWebsites'),
    path('websites/<str:id>', views.getWebsite, name='getWebsite'),
    path('websites/<str:id>/update/', views.updateWebsite, name='updateWebsite'),
    path('websites/create', views.newWebsite, name='newWebsite'),
    path('', WebsiteListView.as_view(), name='website_list'),
    path('create_website', WebsiteCreateView.as_view(), name='create_website'),
    path('<pk>/', WebsiteUpdateView.as_view(), name='website_detail'),
   
]
