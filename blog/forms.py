"""Forms for managing crud for Journal"""
from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
