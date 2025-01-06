from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list' ),
    path('movie_detail/<int:id>/', views.movie_detail, name='movie_detail'),
    path('greeting/', views.greeting, name='greeting'),
    path('emoji/', views.many_emoji, name='emodji'),
    path('image/', views.gif_image, name='image'),
]