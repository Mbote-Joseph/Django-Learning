import re
from django.shortcuts import render
from datetime import datetime
from django.http import Http404

from .models import Notes

# Create your views here.
def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})

def list(request):
    notes = Notes.objects.all()
    return render(request, 'notes/list.html', {'notes': notes, 'today': datetime.today()})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        # raise Http404("Note does not exist")
        return render(request, 'notes/error.html', {'today': datetime.today()})
    return render(request, 'notes/detail.html', {'note': note, 'today': datetime.today()})