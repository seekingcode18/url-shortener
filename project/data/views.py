from django.shortcuts import render
from data.models import Urls, UrlsAuth
from data.serializers import UrlsSerializer, UrlsAuthSerializer
from rest_framework import generics
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect

class UrlsListCreate(generics.ListCreateAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer

class UrlsListCreateAuth(generics.ListCreateAPIView):
    queryset = UrlsAuth.objects.all()
    serializer_class = UrlsAuthSerializer

class UrlsDelete(generics.DestroyAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer

class UrlsDeleteAuth(generics.DestroyAPIView):
    queryset = UrlsAuth.objects.all()
    serializer_class = UrlsSerializer

def url_redirect(request, pk):
    long_url = Urls.objects.get(short_url=pk)
    return redirect(str(long_url))

def url_auth_redirect(request, pk):
    long_url = UrlsAuth.objects.get(short_url=pk)
    return redirect(str(long_url))

class UsersUrlsList(generics.ListAPIView):
    serializer_class = UrlsAuthSerializer
    
    def get_queryset(self):
        user = self.kwargs['id']
        return UrlsAuth.objects.filter(user)