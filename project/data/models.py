from django.db import models
from django.conf import settings

def pkgen():
    import secrets
    return secrets.token_hex(3)


class Urls(models.Model):
    short_url = models.CharField(max_length = 6, primary_key = True, default = pkgen)
    long_url = models.CharField(max_length = 500)

    def __str__(self):
        return self.long_url


class UrlsAuth(models.Model):
    short_url = models.CharField(max_length = 6, primary_key = True, default = pkgen)
    long_url = models.CharField(max_length = 500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.long_url
