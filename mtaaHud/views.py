from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *
import datetime as datetime
import json
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):

    return render(request,"Hood/homepage.html")

def information(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    information = Information.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/information.html', {"information":information})
