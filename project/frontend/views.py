from django.shortcuts import render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests
import http
import json

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

    