from django import forms
from .models import *


class createYTForm(forms.ModelForm):

    class Meta:
        model = YoutubeIdeas
        fields = '__all__'
        

        

        