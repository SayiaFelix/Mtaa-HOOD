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
    return render(request,"Hood/homepage.html")

@login_required
def join_hood(request):
    return render(request,"Hood/join.html")

@login_required
def information(request):
    current_user = request.user
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    informations = Information.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/info.html', {"informations":informations})

@login_required
def add_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
            messages.success(request, 'You Have succesfully created a hood.Now proceed and join a hood')

        return redirect('update-profile')
    else:
        form = HoodForm()

    return render(request, 'update/update_hood.html', {"form": form})

@login_required
def post(request):
    current_user=request.user
    profile = Profile.objects.get(user=current_user)
    posts = Post.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/posts.html', {"posts":posts})

@login_required
def view_post(request, id):
  
    try:
        comments = Comment.objects.filter(post_id=id)
    except:
        comments = []

    blog = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.user
            comment.post = blog
            comment.save()

        return redirect('post')

    else:
        form = CommentForm()
        return render(request,  'Hood/view_post.html', {"blog":blog, "form":form, "comments":comments})


@login_required
def health(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    healthservices = Health.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/healthservices.html', {"healthservices":healthservices})

@login_required
def services(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    securities=Security.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/security.html', {"securities":securities})

@login_required
def businesses(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/businesses.html', {"businesses":businesses})

@login_required
def user_profile(request,profile_id):
     current_user = request.user
     try:
      profile = Profile.objects.get(user=current_user)

     except Profile.DoesNotExist:
      profile = None
     return render(request,"profile/profile.html",{"profile":profile})

@login_required
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
            return redirect('homepage')
    else:
         form = UserRegisterForm()
    return render (request,'registration/register.html',{'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required
def search(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_post(search_term)
        message = f"{search_term}"

        return render(request, 'Hood/search.html', {"message":message, "posts":searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'Hood/search.html', {"message":message})

@login_required
def add_business(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.neighbourhood = profile.neighbourhood
            business.save()

        return HttpResponseRedirect('/businesses')

    else:
        form = BusinessForm()

    return render(request, 'update/update_buss.html', {"form":form})

@login_required
def add_info(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)

    if request.method == "POST":
        form = InformationForm(request.POST, request.FILES)
        if form.is_valid():
            information = form.save(commit=False)
            information.author = current_user
            information.neighbourhood = profile.neighbourhood
            information.save()

        return HttpResponseRedirect('/information')

    else:
        form =  InformationForm()

    return render(request, 'update/update_info.html', {"form":form})

@login_required
def add_post(request):
    current_user = request.user
    profile = Profile.objects.get(user =current_user)

    if request.method == 'POST':
        form  = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.username = current_user
            post.neighbourhood = profile.neighbourhood
            post.save()

        return HttpResponseRedirect('/post')

    else:
        form = PostForm()

    return render(request, 'update/update_post.html', {"form":form})

