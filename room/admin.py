from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message              #*  in order to view your model in admin page

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
