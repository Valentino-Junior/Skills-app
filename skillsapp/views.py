import profile
from django.shortcuts import render,redirect
from .models import Profile
from .forms import UploadForm
from django.db.models import Q
from django.db.models.base import ObjectDoesNotExist 
from django.http  import HttpResponse,Http404

def home(request):
    profiles = Profile.objects.all()
    ctx = {'profiles':profiles}
    return render(request,'profiles/home.html',ctx)

def new_profile(request):
 
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save()
            profile.save()
           
            return redirect('/')
    else:
        form = UploadForm()
    ctx = {
        'form':form
    }
    
    return render(request,'profiles/upload_picture.html',ctx)

def query_skill(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    profiles = Profile.objects.filter(
        Q(skill__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        ) 
    message = f"{q}"
    return render(request, 'profiles/search.html',{"message":message,"profiles": profiles})


def search_results(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_profiles = Profile.search_by_skill(search_term)
        message = f"{search_term}"

        return render(request, 'profiles/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'profiles/search.html',{"message":message})
  
