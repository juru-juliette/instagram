from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    photo=models.ImageField(upload_to='pic/')
    bio=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    follow=models.NullBooleanField(default=False)


    
    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()

class Image(models.Model):
     name=models.CharField(max_length=100)
     image=models.ImageField(upload_to = 'pic/')
     caption=HTMLField()
     likes=models.IntegerField(null=True,default=0)
     comment= models.TextField()
     pub_date = models.DateTimeField(auto_now_add=True)
     profile=models.ForeignKey(Profile, null=True)
     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
     def save_image(self):
         self.save()

     def delete_image(self):
       self.delete()
       
     def update_caption(self,cap):
         self.caption=cap
         self.save() 


class Follow(models.Model):
     follower=models.ForeignKey(Profile, related_name='follower')
     following=models.ForeignKey(Profile ,related_name='followee')

