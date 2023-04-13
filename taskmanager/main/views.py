from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Tasks
from .forms import TasksForm
# Create your views here.

def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'main/index.html', {'title': 'HOME', 'tasks':tasks})

def about(request):
    return render(request, 'main/about.html')

def aviata(request):
    return render(request, 'main/aviata.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Incorrect format'
    form = TasksForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


