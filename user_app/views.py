from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def Login(request):

    form = UserCreationForm()
        


    context = {}

    return render(request, 'user_app/login.html', context)



def CreateUser(request):

    form = UserCreationForm()
    context = {}
    

    return render(request, 'user_app/create_user.html', context)