from django.shortcuts import render
from data.models import Urls
from data.serializers import UrlsSerializer
from rest_framework import generics
from django.http import HttpResponse, HttpResponseNotFound

class UrlsListCreate(generics.ListCreateAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer


class UrlsDelete(generics.DestroyAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer

def url_redirect(request, pk):
    long_url = Urls.objects.get(short_url=pk)
    return HttpResponse(long_url)
