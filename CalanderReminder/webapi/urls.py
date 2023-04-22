from django.urls import path
from webapi import views

urlpatterns = [
    path('add_user', views.addFriends),
]