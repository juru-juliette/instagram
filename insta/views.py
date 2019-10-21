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
def profile(request):
     current_user = request.user
     if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect('profile')

     else:
        form = ProfileForm()
     return render(request, 'IG/profile.html', {"form": form})
@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    picture = Profile.objects.filter(username = current_user)
    return render(request, 'IG/edit_profile.html', { "picture":picture})
@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'IG/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'IG/search.html',{"message":message})

     
def search_by_username(name):
       users=User.objects.filter(username__icontains=name)
       return users