from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from . forms import UserUpdateForm, ProfileUpdateForm
# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} is created! You can log in to your accout!')

            return redirect('login')

    else:
        form = UserCreationForm()

    content_dict ={'form': form}
    return render(request, 'users/register.html',content_dict)

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)  # all user profiel except for your own
    context_dict = {"profiles":profiles}
    return render(request, "users/profile_list.html", context_dict)  

@login_required
def profile(request):
    profile = Profile.objects.all()
    #u_form = UserUpdateForm(instance=request.user)
    #p_form = ProfileUpdateForm(instance=request.user.profile)
    follows = Profile.objects.all()
    context_dict = {"profile":profile,"follows":follows}
    #context_dict = {"profile":profile,"u_form":u_form, "p_form:":p_form}
    return render(request, 'users/profile.html',context_dict)


