from django.db import models
from django.contrib.auth.models import User

class BlogUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    bio = models.TextField()
    headshot=models.ImageField()
    # other fields related to BlogUser
