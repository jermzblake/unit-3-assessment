from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def tasks_index(request):
    task_list = Task.objects.all()
    #instantiate TaskForm to be rendered in the template
    task_form = TaskForm()
    return render(request, 'index.html', {
        'task_list': task_list,
        'task_form':task_form
        })
