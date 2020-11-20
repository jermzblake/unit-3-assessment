from django.shortcuts import render
from .models import Task

def tasks_index(request):
    task_list = Task.objects.all()
    return render(request, 'index.html', {'task_list': task_list})
