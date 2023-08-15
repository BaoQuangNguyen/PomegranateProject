from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from. models import Task, Status
from .forms import StatusForm


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
    status_form = StatusForm()
    return render(request, 'tasks/detail.html', {
        'task': task, 'status_form': status_form
    })

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'notes']
    template_name = 'main_app/task_form.html'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['due_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

class TaskUpdate(UpdateView):
    model = Task
    fields = ['description', 'due_date', 'notes']

class TaskDelete(DeleteView):
    model = Task
    success_url = '/tasklist'

def update_status(request, task_id):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.task_id = task_id
        new_status.is_latest = True  # Mark as the latest status
        new_status.save()

        # Update the completed_at and total_time_spent attributes of the task
        task = Task.objects.get(pk=task_id)
        task.completed_at = new_status.created
        task.total_time_spent = new_status.pomegranates_completed * 1500  # 25 minutes per pomegranate
        task.save()

        # Mark previous statuses as not latest
        previous_statuses = Status.objects.filter(task=task).exclude(pk=new_status.pk)
        previous_statuses.update(is_latest=False)

        # Render the task results template
        return render(request, 'task_results.html', {'status': new_status})

    return redirect('detail', task_id=task_id)


def timer(request):
    task_id = request.GET.get('task')  # Get the selected task's ID from query parameters
    print('Received task_id:', task_id)  # Add this line to print the task_id
    if task_id:
        current_task = Task.objects.get(pk=task_id)
    else:
        current_task = None
    return render(request, 'timer.html', {'current_task': current_task})

def task_results(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    latest_status = Status.objects.filter(task=task, is_latest=True).first()  # Get the latest status
    return render(request, 'task_results.html', {
        'task': task,
        'status': latest_status,
    })

def break_timer(request):
    task_id = request.GET.get('task')  # Get the selected task's ID from query parameters
    if task_id:
        current_task = Task.objects.get(pk=task_id)
    else:
        current_task = None
    return render(request, 'breaktimer.html', {'current_task': current_task})




