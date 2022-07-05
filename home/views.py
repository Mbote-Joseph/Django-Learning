from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Hello, world. You're at the home page.</h1>")


def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})

















# def about(request):
#     return HttpResponse("Welcome to Django! About Page")

# def contact(request):
#     return HttpResponse("Please enter your email address.")


# def email(request):
#     return HttpResponse("Thank you for your email.")