from django.test import TestCase
from .models import Image,Profile
# Create your tests here.
class ImageTestClass(TestCase):
        def setUp(self):
          
          self.profile=Profile(id=1,photo='Rwanda',bio='Kigali')
          self.image=Image(id=1,image='@style',name='hair',caption="new look",likes=2,profile=self.profile)
        def test_save_image(self):
          self.image.save_image()
          images = Image.objects.all()
          self.assertTrue(len(images) > 0)  

        def tearDown(self):
           Profile.objects.all().delete()
           Image.objects.all().delete()
        def test_delete_image(self):
           self.image.save_image()
           self.image.delete_image()
           images = Image.objects.all()
           self.assertTrue(len(images) == 0) 
        def test_update_caption(self):
           self.image.save_image()
           caption='new look'
           self.image.update_caption(caption)
           self.assertTrue( self.image.caption == caption) 

class ProfileTestClass(TestCase):
        def setUp(self):
          
          self.profile=Profile(id=1,photo='Rwanda',bio='Kigali')
          self.image=Image(id=1,image='@style',name='hair',caption="new look",likes=2,profile=self.profile)
        def test_save_profile(self):
          self.profile.save_profile()
          profiles = Profile.objects.all()
          self.assertTrue(len(profiles) > 0) 