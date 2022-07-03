from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

def about(request):
    return HttpResponse("Welcome to Django! About Page")

def contact(request):
    return HttpResponse("Please enter your email address.")


def email(request):
    return HttpResponse("Thank you for your email.")