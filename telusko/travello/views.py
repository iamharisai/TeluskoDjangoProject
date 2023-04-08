from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.price = 700
    dest1.desc = 'My first job city'
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Bangaluru'
    dest2.price = 900
    dest2.desc = 'Beautiful city'
    dest2.img = 'destination_2.jpg'
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Pune'
    dest3.price = 500
    dest3.desc = 'My dream job city'
    dest3.img = 'destination_3.jpg'
    dest3.offer = True
    
    dests = [dest1,dest2,dest3]

    return render(request,'index.html',{'dests': dests})

