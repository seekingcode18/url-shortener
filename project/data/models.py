from django.db import models

def pkgen():
    import secrets
    return secrets.token_hex(3)

class long_url_manager(models.Manager):
    def check_url()


class Urls(models.Model):
    short_url = models.CharField(max_length = 6, primary_key = True, default = pkgen)
    # if url is valid, write to db
    # else, return 'not valid' error
    long_url = models.CharField(max_length = 500)

    def __str__(self):
        return self.long_url
