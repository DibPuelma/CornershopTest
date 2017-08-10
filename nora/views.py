from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def menu_index(request):
    return HttpResponse("Hello, world. You're at the menu index.")
