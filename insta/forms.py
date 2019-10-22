from django import forms
from .models import Image,Profile
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile', 'pub_date','likes','comment']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username','follow']
class NewCommentForm(forms.Form):
    comment = forms.CharField(label='Comment',max_length=600)