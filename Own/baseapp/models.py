import uuid
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.

class Pictures(models.Model):
        church_pic = models.ImageField(upload_to='church_pics',blank=True)

        def __str__(self):
            return self.church_pic

class Post(models.Model):
        author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
        title = models.CharField(max_length = 246)
        text = models.TextField()
        create_date = models.DateTimeField(default=timezone.now)

        def get_absolute_url(self):
            return reverse("pictures:post_detail", kwargs={'pk':self.pk})

        def __str__(self):
            return self.title

class Profile_pic(models.Model):
        Priest_Name= models.CharField(max_length=246,blank=True)
        Parishpriest_pic = models.ImageField(upload_to='profile',blank=True)
        Description = models.TextField(blank=True)

        def __str__(self):
            return self.Priest_Name

        def delete(self,*args,**kwargs):
            self.Parishpriest_pic.delete()
            super().delete(*args,**kwargs)




class Notices(models.Model):
        title = models.CharField(max_length = 50)
        file = models.FileField(upload_to='notices')
        create_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.title

        def delete(self,*args,**kwargs):
            self.file.delete()
            super().delete(*args,**kwargs)

class Lectors(models.Model):
        title=models.CharField(max_length=246)
        file=models.FileField(upload_to='lectors')

        def __str__(self):
            return self.title

        def delete(self,*args,**kwargs):
            self.file.delete()
            super().delete(*args,**kwargs)


class News(models.Model):
        title = models.CharField(max_length=50)
        upload = models.FileField(upload_to='albums/')
        description = models.TextField()
