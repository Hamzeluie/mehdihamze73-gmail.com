from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    create_date = models.DateField(auto_now_add=True)

