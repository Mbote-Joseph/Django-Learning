import re
from django.shortcuts import render
from datetime import datetime
from django.http import Http404

# For class based Views
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NotesForm
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

 # Class Based Views
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.today()
        return context

class AuthView(LoginRequiredMixin ,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.today()
        return context

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/list'
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/list'
    form_class = NotesForm
    
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/list'
    def get_object(self):
        return Notes.objects.get(pk=self.kwargs['pk'])