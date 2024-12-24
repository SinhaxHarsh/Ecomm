from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import Profile
from base.emails import send_account_activation_email

def login_page(request):
    if request.method=='POST':
        email= request.POST.get('email')
        password= request.POST.get('password')
        user= User.objects.filter(email=email)
        if not user.exists():
            messages.warning(request,'Account Not Found')
            return HttpResponseRedirect(request.path_info)
        user_obj= authenticate(username=email,password=password)
        if not user_obj:
            login(request, user_obj)
            return redirect('/')
        messages.warning(request,'Invalid Credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request,'accounts/login.html')

def register_page(request):
    if request.method=='POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        password= request.POST.get('password')

        user_obj= User.objects.filter(username= password)

        if user_obj.exists():
            messages.warning(request,'Email Is Already In Use')
            return HttpResponseRedirect(request.path_info)
        user_obj= User.objects.create(first_name= first_name,last_name=last_name,email=email,password=password)
        user_obj.set_password(password)
        user_obj.save()
        user= User.objects.get(email= email)
        user.is_email_verified= True
        messages.success(request,'An Email Has Been Sent On Your Email')
        send_account_activation_email(email)
        return HttpResponseRedirect(request.path_info)

    return render(request,'accounts/register.html')
