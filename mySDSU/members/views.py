from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView
from .forms import appointmentForm
from .forms import applyGradForm
from .models import Classes
from .models import Grades 

# Create your views here.
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

@login_required
def homePage(request):
    submitted = False
    if request.method == "POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/homepage?submitted = True')
    else:
        form = appointmentForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'homepage.html', {'form':form, 'submitted':submitted})

@login_required
def myClasses(request):
    class_list = Classes.objects.filter(students = request.user)
    return render(request, 'myClasses.html', {'class_list': class_list})

@login_required
def myGrades(request):
    grade_list = Grades.objects.filter(students = request.user)
    return render(request, 'myGrades.html', {'grade_list': grade_list})

@login_required
def applyToGrad(request):
    submitted = False
    if request.method == "POST":
        form = applyGradForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/applyToGrad?submitted = True')
    else:
        form = applyGradForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'applyToGrad.html', {'form':form, 'submitted':submitted})

@login_required
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