from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from. models import Task



# Create your views here.

def home(request):
    return render(request, 'home.html')

def tasklist(request):
    return render(request, 'tasklist.html')

def tasks_index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {
        'tasks': tasks
    })

def tasks_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'tasks/detail.html', {
    'task': task
  })

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date']
    template_name = 'main_app/task_form.html'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['due_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

class TaskUpdate(UpdateView):
    model = Task
    fields = ['description', 'due_date']

class TaskDelete(DeleteView):
    model = Task
    success_url = '/tasklist'


def timer(request):
    task_id = request.GET.get('task')  # Get the selected task's ID from query parameters
    print('Received task_id:', task_id)  # Add this line to print the task_id
    if task_id:
        current_task = Task.objects.get(pk=task_id)
    else:
        current_task = None
    return render(request, 'timer.html', {'current_task': current_task})


def break_timer(request):
    task_id = request.GET.get('task')  # Get the selected task's ID from query parameters
    if task_id:
        current_task = Task.objects.get(pk=task_id)
    else:
        current_task = None
    return render(request, 'breaktimer.html', {'current_task': current_task})



