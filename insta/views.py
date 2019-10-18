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

# @login_required(login_url='/accounts/login/')
# def image(request,article_id):
#     try:
#         image = Image.objects.get(id = image_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"home.html", {"image":image})