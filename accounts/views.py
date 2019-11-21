from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import reg
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method=="POST":
        lemail = request.POST['lemail']
        lpass1 = request.POST['lpassword']
        user=auth.authenticate(username=lemail,password=lpass1)
        if user is not None:
            print("success")
            auth.login(request,user)

            return redirect("home after login")
        else:
            print("fail")
            messages.info(request,"invalid credentials")
            return redirect("login")

    else:
        return render(request,"login1.html")




def register (request):
    if request.method =="POST":
        fullName=request.POST['name']
        email = request.POST['email']
        ph = request.POST['number']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=fullName).exists():
                messages.info(request,'please change username ')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'please change email')
                return redirect('register')
            else:
                user = User.objects.create_user(username=fullName, email=email, password=pass1)
                user.save()
                add = reg(username=fullName, email=email, phone=ph, password=pass1)
                add.save()
                print("user created")

        else:
            messages.info(request, 'password incorrect')
            return redirect('register')


        return redirect('home after login')

    else:
        return render(request,"signup1.html")

def home(request):
    return render(request,'home.html')


def logout(request):
    auth.logout(request)
    return redirect("home after login")


def recap(request):
    return render(request,"lines1.html")