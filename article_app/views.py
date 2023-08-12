from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from . models import *
from django.contrib import messages
# Create your views here.
from .forms import *


class ArticleCreateView(CreateView):
    model = Article
    fields = '__all__'
    
    template_name = 'article_app/create_article.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


def create_article(request):
        if request.method == 'POST':
            article = CreateArticleForm(instance=request.article, prefix='article')
            website = WebsiteForm(instance=request.website, prefix='website')
            if article.is_valid() and website.is_valid():
                article.save()
                website.save()
                messages.info(request, 'Article created successfully')
                return render(request, '/')
        else:
            article = CreateArticleForm(instance=request.article, prefix='article')
            website = WebsiteForm(instance=request.website, prefix='website')
        return render(request, 'article_app/create_article.html', {'article': article, 'website':website})







    
    
    
    
    

class ArticleListView(ListView):
    model = Article
    template_name = "article_app/article_list.html"
    context_object_name = 'article'    



class ArticleUpdateView(UpdateView):
    model = Article
    fields = '__all__'
    template_name = 'article_app/article_detail.html'

    def get_success_url(self):
        return self.object.get_absolute_url()
    
    def form_valid(self, form):
        messages.info(self.request, 'Article Updated successfully')
        return super().form_valid(form)