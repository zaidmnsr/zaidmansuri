

from django.urls import path, include
from .  import views
from .views import *



app_name = 'review'



urlpatterns = [
   # path('', PatientListView.as_view(), name='patient_list'),
    path('list/', views.review, name='review_list'),
    path('create_task/', CreateTaskView.as_view(), name='create_review'),
    #path('<pk>/', WebsiteUpdateView.as_view(), name='website_detail'),
    #path('create_patient/load_nurses/', views.load_nurse, name='load_nurses'),

    

   
]
