from django.urls import path
from . import views

urlpatterns = [
    path('greeting/', views.greeting, name='greeting'),
    path('emoji/', views.many_emoji, name='emodji'),
    path('image/', views.gif_image, name='image'),
]