from django import forms
from django.forms import ModelForm
from .models import Article
from .constants import ArticleStatus


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Title'}),
            'content': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Enter Content'}),
            'status': forms.Select(attrs={'class': 'select', 'disabled': True}, choices=ArticleStatus.choices), }
