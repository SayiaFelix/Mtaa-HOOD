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
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user

        try:
          profile = Profile.objects.get(user=current_user)
        except Profile.DoesNotExist:
          profile = None
        # profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('')

    return render(request,"Hood/homepage.html")

def information(request):
    current_user = request.user
    try:
     profile = Profile.objects.get(user=current_user)

    except Profile.DoesNotExist:
      profile = None

    # profile = Profile.objects.get(user=current_user)
    informations = Information.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'Hood/information.html', {"informations":informations})
