from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import DeleteView
from django.db.models import Sum

def tasks_index(request):
    task_list = Task.objects.all()
    #instantiate TaskForm to be rendered in the template
    task_form = TaskForm()
    total_time = Task.objects.aggregate(Sum('time'))
    return render(request, 'index.html', {
        'task_list': task_list,
        'task_form':task_form,
        'total_time':total_time
        })

def add_task(request):
    # create a ModelForm instance using the data in request.POST
    form = TaskForm(request.POST)
    # validate the form
    if form.is_valid():
        form.save()
    return redirect('index')

class TaskDelete(DeleteView):
    model = Task
    success_url = '/'