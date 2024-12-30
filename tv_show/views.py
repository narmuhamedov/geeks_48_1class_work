from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greeting(request):
    if request.method == 'GET':
        return HttpResponse('Hello This is my first Project Django 🤓')
    
def many_emoji(request):
    if request.method == 'GET':
        return HttpResponse('😀 🥶 😥 🥺 🫠 🥱 🤖')

def gif_image(request):
    if request.method == 'GET':
        return HttpResponse("<img src='https://user-images.githubusercontent.com/14011726/94132137-7d4fc100-fe7c-11ea-8512-69f90cb65e48.gif'>")
    