from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        exclude = ['neighbourhood']
        

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


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


        widgets = {
           'username' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
           'email' :forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email Address'}),
           'password1' : forms.TextInput(attrs={'class': 'form-control','placeholder':'password'}),
           'password2' :forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}),
    
        }