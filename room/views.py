from django.shortcuts import render
from .models import Room

# Create your views here.

def home(request):
    rooms =Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'room/home.html',context)

def room(request):
    room =Room.objects.all()
    context = {'room': room}
    return render(request,'room/room.html',context)