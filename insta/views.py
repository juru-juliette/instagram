from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,ProfileForm
from django.contrib.auth.models import User

# from django.http  import HttpResponse
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='Instagram'
    image=Image.objects.all()
    profile = Profile.objects.all()
    return render(request,'home.html',{'title':title , 'image':image, 'profile':profile})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            
            image.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'IG/new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.filter(id=id)
    images = Image.objects.filter(user = user)
   
    return render(request,'IG/my_profile.html',{"profiles":profiles,"user":user,"images":images})

def profile(request):
    current_user = request.user
    # profile=Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # profile.bio=form.cleaned_data['bio']
            # profile.prof_image= form.cleaned_data['prof_image']
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            

        return redirect('IG/my_profile')

    else:
        form = ProfileForm()
    return render(request, 'IG/profile.html', {"form": form})