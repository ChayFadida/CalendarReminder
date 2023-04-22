from django.shortcuts import render
from .models import UsersFriends
# Create your views here.

def check_for_birthday():
    UsersFriends.objects.exclude(all)
    
