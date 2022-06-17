from django import forms
from .models import *

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        exclude = ['user', 'neighbourhood']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['username', 'neighbourhood']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner', 'neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'post']