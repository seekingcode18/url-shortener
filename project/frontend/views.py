from django.shortcuts import render
import requests
import json

def index(request):
    return render(request, 'index.html')


def post(request):
    long_url = request.POST.get("long_url", "")
    response = requests.post('http://localhost:8000/api/urls/', data = {"long_url": str(long_url)})
    if 'short_url' in response.json():
        short_url = response.json()['short_url']
        return render(request, 'index.html', {'short_url': 'http://localhost:8000/{0}'.format(short_url)})

    return render(request,'index.html')

