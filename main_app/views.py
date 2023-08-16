from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, CompletedTask
from django.http import HttpResponseNotAllowed
from django.views.generic import TemplateView



def home(request):
    return render(request, 'home.html')

def tasks_index(request):
    tasks = Task.objects.filter(completed=False)
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

    def get_success_url(self):
        return reverse('index')

class TaskUpdate(UpdateView):
    model = Task
    fields = ['description', 'due_date']

class TaskDelete(DeleteView):
    model = Task
    success_url = '/tasks'

def timer(request):
    task_id = request.GET.get('task')
    print('Received task_id:', task_id)
    if task_id:
        current_task = Task.objects.get(pk=task_id)
    else:
        current_task = None
    return render(request, 'timer.html', {'current_task': current_task})

def break_timer(request):
    task_id = request.GET.get('task') 
    if task_id:
        current_task = Task.objects.get(pk=task_id)
    else:
        current_task = None
    return render(request, 'breaktimer.html', {'current_task': current_task})

def mark_task_completed(request, task_id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    task = Task.objects.get(pk=task_id)

    if not task.completed:
        completed_task = CompletedTask.objects.create(task=task)
        task.completed = True
        task.save()
        update_total_time_spent(task)
        return redirect('completed_task_detail', task_id=task.id)

def completed_task_detail(request, task_id):
    completed_task = CompletedTask.objects.get(task_id=task_id)
    return render(request, 'completedtask.html', {'completed_task': completed_task})

def update_total_time_spent(task):
    task.total_time_spent += 1
    task.save()

class TaskChartView(TemplateView):
    template_name = 'main_app/chart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        completed_tasks = CompletedTask.objects.all()      
        print("Completed Tasks:", completed_tasks)
        context['completed_tasks'] = completed_tasks
        return context

