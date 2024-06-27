from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datatime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileing = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
   
class Post(models.Model):
    id = models.UUIDField(primary_key=True)
    user =  
    image =
    caption = 
    created_at = 
    no_of_likes = 