from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'pic/')
    name = models.CharField(max_length =60)
    post_date = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length =200)
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()
    def delete_image (self):
        self.delete()