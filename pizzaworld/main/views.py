from django.shortcuts import render,redirect
from datetime import datetime
from main.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# Create your views here.
def home(request):
    return render(request,'home.html') 


def contact(request):
    if request.method == 'POST': # to insert data to database
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(username=username,email=email,phone=phone,desc=desc,date=datetime.today()) #object
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request,'contact.html',{'message':"recieved succesfully"})

def about(request):
    return render(request,'about.html') 

def loginUser(request):
    if request.method=="POST":#username-dhruv password Dhruv@12mittal directly added from admin page
        username=request.POST.get("username")
        password=request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/index")
        # A backend authenticated the credentials
    
        else:
            return render(request,'login.html')

    return render(request,'login.html')
def index(request):
    user = request.user
    if user.is_anonymous:
        
        return render(request,'login.html')
    else:
        return render(request,'index.html')
# def logoutUser(request):
#     logout(request)
#     return redirect("/login")