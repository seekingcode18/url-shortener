from django.db import models

def pkgen():
    import secrets
    return secrets.token_hex(3)

class Urls(models.Model):
    short_url = models.CharField(max_length = 6, primary_key = True, default = pkgen)
    long_url = models.CharField(max_length = 500)

