from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.core.mail import send_mail

from django.contrib import messages
# Create your views here.

def base(request):
    return render (request,'base.html')
def home(request):
    return render (request,'index.html')
def about(request):
    return render (request,'about.html')
def do(request):
    return render (request,'do.html')
def contact(request):
    return render (request,'contact.html')
def portfolio(request):
    return render (request,'portfolio.html')

def profile(request):
    return render (request,'profile.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username,email=email,password=password)
        send_mail(
            "Mail from Ansh Website",
            f"Thanks {username} for Signup with us , our team connect with you with in hour ",
            "anshu93172@gmail.com",
            [email],
            fail_silently=False,
        )
        messages.success(request,'User has succesfully created')
        return render (request,'login.html')
    else:
        return render(request, "signup.html")
    
def uuuser():
    s=User.objects.get(username=s)



def login(request):

    if request.method == "POST":
        name = request.POST['name']
        password = request.POST["password"]
        user = authenticate(request,username=name, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are succesfully login in ')
            return render(request, "index.html",{'s':name})
        else:
            messages.error(request,'Invalid User')
            return redirect('login')
    else:
        return render(request, "login.html")


def loogout(request):
    logout(request)
    messages.success(request,'logout succesfully')
    return redirect('base')
