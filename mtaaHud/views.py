from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
import datetime as datetime
import json
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def homepage(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user

        try:
          profile = Profile.objects.get(user=current_user)
        except Profile.DoesNotExist:
          profile = None
        # profile = Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('')

    return render(request,"Hood/homepage.html")

def information(request):
    current_user = request.user
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    # profile = Profile.objects.get(username=current_user)
    informations = Information.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/information.html', {"informations":informations})


def post(request):
    current_user=request.user
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None
    # profile = Profile.objects.get(user=current_user)
    posts = Post.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/posts.html', {"posts":posts})


def view_post(request, id):
    try:
        comments = Comment.objects.filter(post_id=id)
    except:
        comments = []

    posts = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.user
            comment.post = posts
            comment.save()
    else:
        form = CommentForm()
        return render(request, 'Hood/view_post.html', {"posts":posts, "form":form, "comments":comments})


def health(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/healthservices.html', {"healthservices":healthservices})


def services(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    security=Security.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/services.html', {"security":security})


def businesses(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/businesses.html', {"businesses":businesses})

def user_profile(request,profile_id):

    profile = Profile.objects.get(pk = profile_id)
   
    return render(request,"profile/profile.html",{"profile":profile})

def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = ProfileForm()
    return render(request, 'profile/update_user_profile.html', {"form": form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
         login(request, user)
         return redirect('homepage')
        
        else:
            messages.success(request,('Invalid information'))
            return redirect('login')
         
    else:

     return render(request,'registration/login.html')


def register_user(request):
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            

            email = form.cleaned_data['email']
            # send_welcome_email(username,email) 

            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,f'Hello {username}, Your account was Successfully Created.You will receive our email shortly.Thank You!!!')
            return redirect('update-profile')
    else:
         form = UserRegisterForm()
    return render (request,'registration/register.html',{'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
