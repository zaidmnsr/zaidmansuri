from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from . models import *
from.forms import *

# Create your views here.



class YTListView(ListView):
    model = YoutubeIdeas
    template_name = "yt_app/yt_list.html"
    context_object_name = 'yt'



class IdeaCreateView(CreateView):
    model = YoutubeIdeas
    #fields = '__all__'
    form_class = createYTForm
    template_name = 'yt_app/create_yt.html'

    
    
    
    def get_success_url(self):
        return self.object.get_absolute_url()