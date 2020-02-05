from rest_framework import serializers
from data.models import Urls, UrlsAuth

class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'

class UrlsAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlsAuth
        fields = '__all__'