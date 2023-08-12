from django import forms
from .models import *


class createWebsiteForm(forms.ModelForm):

    class Meta:
        model = Website
        fields = '__all__'
        

        

        