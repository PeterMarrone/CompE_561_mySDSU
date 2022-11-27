from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'index.html')

def myClasses(request):
    return render(request, 'myClasses.html')

def myGrades(request):
    return render(request, 'myGrades.html')

def applyToGrad(request):
    return render(request, 'applyToGrad.html')

def externalResources(request):
    return render(request, 'externalResources.html')