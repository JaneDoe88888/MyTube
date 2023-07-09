from django import forms
from .bulma_mixin import BulmaMixin
from .models import Video


class VideoForm(BulmaMixin, forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Придумайте название к видео'}),
                            label='Название к видео')
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Напишите описание к видео'}),
                                  label='Описание к видео')
    image = forms.ImageField(label='Загрузите обложку для видео')
    file = forms.FileField(label='Загрузите ваше видео')

    class Meta:
        model = Video
        fields = ['title', 'description', 'image', 'file']
