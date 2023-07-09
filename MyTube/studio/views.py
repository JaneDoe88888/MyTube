from django.shortcuts import render, redirect
from .forms import *


def home(request):
    videos = Video.objects.all()
    confirm_delete = False
    action = request.GET.get('action')
    if action == 'delete':
        confirm_delete = True
    if request.GET.get('confirm'):
        Video.objects.get(pk=request.GET.get('pk')).delete()
        return redirect('studio:home')
    if action == 'archived':
        video = Video.objects.get(pk=request.GET.get('pk'))
        if video.archived:
            video.archived = False
        else:
            video.archived = True
        video.save()
    return render(request, 'home_studio.html', {'videos': videos, 'confirm_delete': confirm_delete})


def video_create(request):
    form = VideoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('studio:home')
    return render(request, 'video_create.html', {'form': form})


def video_edit(request, pk):
    video = Video.objects.get(pk=pk)
    form = VideoForm(request.POST or None, request.FILES or None, instance=video)
    if form.is_valid():
        form.save()
        return redirect('studio:home')
    return render(request, 'video_create.html', {'form': form})


