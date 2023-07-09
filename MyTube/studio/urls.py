from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('video_create/', views.video_create, name='video_create'),
]