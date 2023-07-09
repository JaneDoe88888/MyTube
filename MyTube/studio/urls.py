from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('video_create/', views.video_create, name='video_create'),
    path('video_edit/<int:pk>', views.video_edit, name='video_edit'),

]