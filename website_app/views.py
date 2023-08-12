from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from . models import *
from.forms import *
from rest_framework.decorators import api_view
from .serializers import WebsiteSerializer
from rest_framework.response import Response

# Create your views here.




@api_view(['GET'])
def getAllWebsites(request):
    website = Website.objects.all()

    serializer = WebsiteSerializer(website, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def getWebsite(request, id):
    website = Website.objects.filter(id=id)
    serializer = WebsiteSerializer(website, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def newWebsite(request):
    
    data = request.data
    website = Website.objects.create(**data)
    serializer = WebsiteSerializer(website, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateWebsite(request, id):
    website = Website.objects.filter(id=id)

    website.website_name = request.data['website_name']

    website.save()

    serializer = WebsiteSerializer(website, many=True)
    return Response(serializer.data)


class WebsiteListView(ListView):
    model = Website
    template_name = "website_app/website_list.html"
    context_object_name = 'website'

    # def get_queryset(self, *args, **kwargs):
    #     # qs = super(WebsiteListView, self).get_queryset(*args, **kwargs)
    #     qs = {'all': qs.objects.all(),
    #           'active': qs.objects.filter(status='Active')
    #           }
              

        
    #     return qs



class WebsiteCreateView(CreateView):
    model = Website
    #fields = '__all__'
    form_class = createWebsiteForm
    template_name = 'website_app/create_website.html'

    
    
    
    def get_success_url(self):
        return self.object.get_absolute_url()
    


class WebsiteUpdateView(UpdateView):
    model = Website
    fields = '__all__'

    template_name = "website_app/website_detail.html"

    
   
   
    def get_success_url(self):
        return self.object.get_absolute_url()
    
    # def form_valid(self, form):
    #     messages.success(self.request, f'Save Completed ! Site has been updated')
    #     return super().form_valid(form)
