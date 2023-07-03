from django.shortcuts import render, redirect
from . models import Video
from . forms import CommentForm


def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})


def video(request, pk):
    video_object = Video.objects.get(pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.video = video_object
        instance.save()
        return redirect('app:video', pk=pk)
    return render(request, 'video.html', {'video': video_object, 'form': form})


def likes(request, pk):
    video_object = Video.objects.get(pk=pk)
    if request.user not in video_object.likes.all():
        video_object.likes.add(request.user)
        video_object.dislikes.remove(request.user)
    elif request.user in video_object.likes.all():
        video_object.likes.remove(request.user)
    return redirect('app:video', pk=pk)


def dislikes(request, pk):
    video_object = Video.objects.get(pk=pk)
    if request.user not in video_object.dislikes.all():
        video_object.dislikes.add(request.user)
        video_object.likes.remove(request.user)
    elif request.user in video_object.dislikes.all():
        video_object.dislikes.remove(request.user)
    return redirect('app:video', pk=pk)