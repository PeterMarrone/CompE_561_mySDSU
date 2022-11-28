from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Students
from .models import Classes
from .models import Grades

# Create your views here.
def homePage(request):
    return render(request, 'homepage.html')

def myClasses(request):
    class_list = Classes.objects.all()
    return render(request, 'myClasses.html', {'class_list': class_list})

def myGrades(request):
    grade_list = Grades.objects.all()
    return render(request, 'myGrades.html', {'grade_list': grade_list})

def applyToGrad(request):
    return render(request, 'applyToGrad.html')

def externalResources(request):
    return render(request, 'externalResources.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.success(request, ("Incorrect Login... Try Again"))
            return redirect('Login')

    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully Logged Out!"))
    return redirect('Login')