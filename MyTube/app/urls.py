from django . urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('video/<int:pk>', views.video, name='video'),
    path('likes/<int:pk>', views.likes, name='likes'),
    path('dislikes/<int:pk>', views.dislikes, name='dislikes'),
    path('comment_likes/<int:pk>', views.comment_likes, name='comment_likes'),
    path('comment_dislikes/<int:pk>', views.comment_dislikes, name='comment_dislikes'),
    path('reply/<int:pk>', views.reply, name='reply'),
]