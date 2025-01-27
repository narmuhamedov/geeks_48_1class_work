from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.views.generic import ListView
# Create your views here.

#Searc
class SearchView(ListView):
    template_name = 'show.html'
    context_object_name = 'movie_list'


    def get_queryset(self):
        return models.Movies.objects.filter(title__icontains=self.request.GET.get('q'))


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context





#Список фильмов
def movie_list(request):
    if request.method == 'GET':
        movie_list = models.Movies.objects.all().order_by('-id')
        slider = models.Slider.objects.all()
        context = {
            'movie_list': movie_list,
            'slider': slider,
        }
        return render(request, template_name='show.html', context=context)
    

def movie_detail(request, id):
    if request.method == 'GET':
        movie_id = get_object_or_404(models.Movies, id=id)
        context = {'movie_id': movie_id}
        return render(request, template_name='show_detail.html', context=context)













def greeting(request):
    if request.method == 'GET':
        return HttpResponse('Hello This is my first Project Django 🤓')
    
def many_emoji(request):
    if request.method == 'GET':
        return HttpResponse('😀 🥶 😥 🥺 🫠 🥱 🤖')

def gif_image(request):
    if request.method == 'GET':
        return HttpResponse("<img src='https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'>")
    