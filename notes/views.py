from django.shortcuts import render
from datetime import datetime

from .models import Notes

# Create your views here.
def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})

def list(request):
    notes = Notes.objects.all()
    return render(request, 'notes/list.html', {'notes': notes})