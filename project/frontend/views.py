from django.shortcuts import render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests
import http
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    return render(request, 'index.html')


def post(request):
    long_url = request.POST.get("long_url", "")
    try:
        r = requests.get(long_url)
        if r.status_code == 200:
            response = requests.post('http://localhost:8000/api/urls/', data = {"long_url": str(long_url)})
            if 'short_url' in response.json():
                short_url = response.json()['short_url']
                return render(request, 'index.html', {'short_url': 'http://localhost:8000/{0}'.format(short_url)})
        else:
            return render(request, 'index.html', {"error": "something went wrong"})
    except:
        return render(request,'index.html', {"error": "please enter a valid url"})

def post_auth(request):
    long_url = request.POST.get("long_url", "")
    try:
        r = requests.get(long_url)
        if r.status_code == 200:
            response = requests.post('http://localhost:8000/api/urls/', data = {"long_url": str(long_url)})
            if 'short_url' in response.json():
                short_url = response.json()['short_url']
                return render(request, 'index.html', {'short_url': 'http://localhost:8000/{0}'.format(short_url)})
        else:
            return render(request, 'index.html', {"error": "something went wrong"})
    except:
        return render(request,'index.html', {"error": "please enter a valid url"})

class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')