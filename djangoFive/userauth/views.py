from django.shortcuts import render
from userauth.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from django import forms

# Create your views here.

def index(request):
    return render(request,'userauth/index.html')


def register(request):
    register=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            print('User ID:   '+str(user))
            user.set_password(user.password)
            #
            print('User ID:   '+str(user))
            profile = profile_form.save(commit=False)
            profile.user=user

            print ('Profile_user ID: '+str(profile.user))

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']


            user = user.save()
            profile.save()

            register=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'userauth/registration.html',{'register':register,'user_form':user_form,'profile_form':profile_form})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def user_login(request):
    if request.method=="POST":

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:

            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))
            else:
                print('Account Not Active')
                return HttpResponse("Account Not Active")
        else:
            print('Someone Try to Login and Failed')
            print("Username {} and password {}".format(username,password))
            return HttpResponse("Invalid Login detail Supplied!")
    else:
        print('last')
        return render(request,'userauth/login.html',{})
    # return render(request,'userauth/login.html',{})
