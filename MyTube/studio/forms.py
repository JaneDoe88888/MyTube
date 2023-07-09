from django import forms
from .bulma_mixin import BulmaMixin
from .models import Video

class VideoForm(BulmaMixin, forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Придумайте название к видео'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Напишите описание к видео'}))
    image = forms.ImageField()
    file = forms.FileField()

    class Meta:
        model = Video
        fields = ['title', 'description', 'image', 'file']
