from django.urls import path
#from .views import RoomListView, RoomDetailView, RoomCreateView, RoomUpdateView, RoomDeleteView
from . import views 

urlpatterns =[
    #path('', views.home, name = "home"),
    path('room/', views.room, name="room"),
    #path('room/<int:pk>', views.room, name="room"),
    #path('', views.room, name ='room'),

    #path('create-room/', views.createRoom, name="create-room")



    # path('',RoomListView.as_view(), name='home-list'),
    # path('/<int:pk>/', RoomDetailView.as_view(), name="room-detail"),
    # path('new/', RoomCreateView.as_view(), name="room-create"),
    # path('/<int:pk>/update/', RoomUpdateView.as_view(), name="room-update"),
    # path('/<int:pk>/delete/', RoomDeleteView.as_view(), name="room-delete"),
]