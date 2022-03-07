from django.urls import path
from .views import profile_list, profile

app_name = 'users'

urlpatterns = [

    path("profile_list/", profile_list, name="profile_list"),
    path("profile/", profile, name="profile"),
]