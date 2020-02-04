from django.shortcuts import render
from data.models import Urls
from data.serializers import UrlsSerializer
from rest_framework import generics

class UrlsListCreate(generics.ListCreateAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer
    

class UrlsDelete(generics.DestroyAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer