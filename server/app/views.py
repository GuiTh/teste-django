from django.shortcuts import render

def home(req):
    return render(req,'usuarios/home.html' )
# Create your views here.
