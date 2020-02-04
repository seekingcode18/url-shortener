from rest_framework import serializers
from data.models import Urls

class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'