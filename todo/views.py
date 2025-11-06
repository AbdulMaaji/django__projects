from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        if 'add_task' in request.POST:
            new_task = request.POST.get('task')
            if new_task:
                Task.objects.create(title=new_task)
        elif 'clear_tasks' in request.POST:
            Task.objects.all().delete()
        return redirect('index')
    return render(request, 'todo_tasks/index.html', {'tasks': tasks})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')
