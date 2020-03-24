from django.db import models
from django.contrib import auth
# Create your models here.
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

# class NewUser(auth.models.User, auth.models.PermissionsMixin):
#     user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
