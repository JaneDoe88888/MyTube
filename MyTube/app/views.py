from django.shortcuts import render
from . models import Video


def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})
