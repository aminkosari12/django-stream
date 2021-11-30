from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    sign_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
