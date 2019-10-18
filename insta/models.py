from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    prof_image = models.ImageField(upload_to = 'pic/')
    bio = models.CharField(max_length =200)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'pic/')
    name = models.CharField(max_length =60)
    caption=HTMLField()
    post_date = models.DateTimeField(auto_now=True)
    likes=models.IntegerField(null=True,default=0)
    comment=models.TextField(max_length=200)
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()
    def delete_image (self):
        self.delete()
