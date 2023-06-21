from django.shortcuts import render
from . models import Video


def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})

def video(request, pk):
    video_object = Video.objects.get(pk=pk)
    return render(request, 'video.html', {'video': video_object})
