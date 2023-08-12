from django import forms
from .models import *
from website_app.models import Website


class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ['main_keyword']



class WebsiteForm(forms.ModelForm):

    class Meta:
        model = Website
        fields = ['website_name']
        

        

        