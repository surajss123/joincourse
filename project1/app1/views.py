from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from app1.models import condact_info
from django.contrib import messages

# Create your views here.


def sign_Up(request):
    return render(request, "Sign_Up.html")



def signUp(request):
    
    if request.method == "POST":
        uName = request.POST['username']
        e_mail = request.POST['email']
        passwrd = request.POST['password']
        conf_passwrd = request.POST['conf-password']
        # print(uName,e_mail,passwrd,conf_passwrd)
        if User.objects.filter(username=uName):
            messages.error(request,'Username already taken')
            return redirect('signup')
        elif User.objects.filter(email=e_mail).exists():
            messages.error(request,'Email already exists')
            return redirect('signup')

        elif passwrd != conf_passwrd:
            messages.error(request,'Password not equal to Confirm Password')
            return redirect('signup')
            
           
        else:
            myuser = User.objects.create_user(uName, e_mail, passwrd)
            myuser.save()
            messages.success(request,"Your Account has been sucessfully Created")
            return redirect('signup')
            # return redirect('home')

        

        
    return render(request,"Sign_Up.html")

def signIn(request):
    if request.method == 'POST':
        uName = request.POST['username']
        pass1 = request.POST['password']
        print(uName,pass1)

        user = authenticate(username=uName, password=pass1)
        if user is not None:
            print('hello')
            login(request,user)
            fname = user.first_name
            return render(request,"home.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('signin')

    return render(request,"Sign_In.html")

def sura4(request):

    return render(request,"home.html")

def navbar(request):
    return render(request,"navbar.html")

def about(request):
    return render(request,"about.html")

def course(request):
    return render(request,"course.html")

def condact(request):
    if request.method == 'POST':
        Name = request.POST.get("name")
        Condact_Number = request.POST.get("condact_number")
        Email_id = request.POST.get("email")
        City = request.POST.get("city")
        Course_Details = request.POST.get("courses")
        print(Name,Condact_Number,Email_id,City,Course_Details)
        data = condact_info(Name=Name,Condact_Number=Condact_Number,Email_id=Email_id,City=City,Course_Details=Course_Details)
        data.save()
    return render(request,"condact.html")