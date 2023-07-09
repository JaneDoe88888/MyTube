from django.shortcuts import render, redirect
from . models import Comment
from . forms import CommentForm
from studio.models import Video


def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})


def video(request, pk):
    video_object = Video.objects.get(pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        if not request.user.is_authenticated:
            return render(request, 'error.html', {})
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


def comment_likes(request, pk):
    comment = Comment.objects.get(pk=pk)
    if not request.user.is_authenticated:
        return render(request, 'error.html', {})
    if request.user not in comment.likes.all():
        comment.likes.add(request.user)
        comment.dislikes.remove(request.user)
    elif request.user in comment.likes.all():
        comment.likes.remove(request.user)
    return redirect('app:video', pk=comment.video.pk)


def comment_dislikes(request, pk):
    comment = Comment.objects.get(pk=pk)
    if not request.user.is_authenticated:
        return render(request, 'error.html', {})
    if request.user not in comment.dislikes.all():
        comment.dislikes.add(request.user)
        comment.likes.remove(request.user)
    elif request.user in comment.dislikes.all():
        comment.dislikes.remove(request.user)
    return redirect('app:video', pk=comment.video.pk)


def reply(request, pk):
    parent_comment = Comment.objects.get(pk=pk)
    form = CommentForm(request.POST or None)
    show_replies = request.GET.get('replies')
    if show_replies:
        replies = Comment.objects.filter(parent=parent_comment)
        return render(request, 'replies.html', {'replies': replies})
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.video = parent_comment.video
        instance.parent = parent_comment
        instance.save()
        return redirect('app:video', pk=parent_comment.video.pk)
    return render(request, 'reply.html', {'form': form})


