from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def Login(request):

            if request.method == 'POST':
                form = AuthenticationForm(request, data=request.POST)
                if form.is_valid():    
                    user = form.get_user()
                    login(request, user)
                    return redirect('core_app:core_dashboard')
  
            form = AuthenticationForm(request)
            context = {'form': form}
            return render(request, 'account_app/login.html', context)

   
def Logout(request):
  
        if request.method == 'POST':
            logout(request)
            messages.info(request, 'You have been logged out')
            return redirect('account_app:login')
   

def CreateUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "User created successfully")
            return redirect('account_app:login')
        else:
            messages.warning(request, 'Something went wrong ')
            return redirect('account_app:create_user')
    else:
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'account_app/create_user.html', context)


def ChangePasswords(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.info(request, 'Pass Updated')
            return redirect('core_dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('password_change')
    else:
        form = PasswordChangeForm
        context = {'form': form}
        return render(request, 'account_app/password_change', context)
