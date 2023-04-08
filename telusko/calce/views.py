from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("<h1>Hello world!</h1>")
    return render(request,'home.html',{'name': 'Harisai'})

def add(request):

    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    result = val1 + val2

    return render(request, "results.html",{'result': result})  