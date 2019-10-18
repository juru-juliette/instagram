from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm

# from django.http  import HttpResponse
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    title='Instagram'
    image=Image.objects.all()
    return render(request,'home.html',{'title':title , 'image':image})

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
    return render(request, 'new_post.html', {"form": form})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})