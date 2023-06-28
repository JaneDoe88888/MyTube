from django . urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('video/<int:pk>', views.video, name='video'),
    path('likes/<int:pk>', views.likes, name='likes'),
    path('dislikes/<int:pk>', views.dislikes, name='dislikes'),
]