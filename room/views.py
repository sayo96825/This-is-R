from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Room
#from .forms import RoomForm

# Create your views here.

def home(request):
    rooms =Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'room/home.html',context)

# def createRoom(request):
#     form = RoomForm()
#     context = {'form':form}
#     return render(request, 'room/room_form.html', context)

# class RoomListView(ListView):
#     model = Room
#     template_name = 'room/room.html'
#     context_object_name ='room'
#     ordering = ['-created']

# class RoomDetailView(DetailView):
#     model = Room

# class RoomCreateView(CreateView):
#     model = Room
#     fields = ['host', 'name']

#     def form_valid(self,form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Room
#     feidls = ['host','name']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
        
# class RoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Room
#     success_url = '/'

#     def test_func(self):
#         room = self.get_object()
#         if self.request.user == room.host:
#             return True
#         return False



def room(request):
        room =Room.objects.all()
        context = {'room': room}

        return render(request,'room/room.html',context)

# def room(request, pk):
#         room =Room.objects.get(id=pk)
#         context = {'room': room}
#         return render(request,'room/room.html',context)