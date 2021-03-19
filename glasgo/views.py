from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!\n<a href='/glasgo/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page.")

def log_in(request):
    return HttpResponse("Login page")

def sign_up(request):
    return render(request, 'glasgo/signup.html')
