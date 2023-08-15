from django.contrib.auth.forms import UserCreationForm
from .models import Teacher, Post
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('username', 'password1', 'password2', 'license')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
