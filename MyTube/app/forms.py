from django import forms
from . models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'comment_input', 'placeholder': 'Введите комментарий'}))

    class Meta:
        model = Comment
        fields = ['text',]