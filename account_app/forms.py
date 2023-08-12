from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']





# class LoginUserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         required_fields = ['username', 'password']

