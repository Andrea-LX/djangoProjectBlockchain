from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import RegisterForm, LoginForm
from django.urls import reverse
from django.contrib import messages
from user.models import Post

def getIP(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip


def log(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            lastIp = UserProfile.objects.get(user=user)
            if not lastIp.ipAddress == getIP(request):
                messages.warning(request, str(user) + ': Different IP. I proceed to update.')
            try:
                lastIp.ipAddress = getIP(request)
                lastIp.save()
            except:
                messages.success(request, 'Unable to update IP address.')
            finally:
                messages.success(request, str(user) + ': Old and new IP used for login are the same. Updated data.')
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('/governance/')
                else:
                    login(request, user)
                    return redirect('/home/')
    else:
        form = LoginForm()
        return render(request, 'login/login.html', {'form':form})

def registration(request):
    try:
        ip = getIP(request)
    except:
        ip = None

    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        thisUser = UserProfile()
        thisUser.user = user
        thisUser.ipAddress = ip
        thisUser.save()
        return redirect('/login/')
    else:
        form = RegisterForm()
        return render(request, 'login/registration.html', {'form':form})

def controlUser(request, pk):
    user = User.objects.filter(id=pk).values()
    return render(request, 'login/url_page.html', {'user':user})