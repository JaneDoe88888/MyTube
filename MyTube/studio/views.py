from django.shortcuts import render, redirect
from .forms import *


def home(request):
    videos = Video.objects.all()
    return render(request, 'home_studio.html', {'videos': videos})


def video_create(request):
    form = VideoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('studio:home')
    return render(request, 'video_create.html', {'form': form})
