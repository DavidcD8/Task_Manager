from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


# Create your views here.

# View to display all tasks
def task_list(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# View to create a new task
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('task_list')  # Redirect back to task list after creation
    return render(request, 'tasks/task_create.html')


#View to update Task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Get the task by primary key (ID)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()  # Save the updated task
        return redirect('task_list')  # Redirect to task list after saving
    return render(request, 'tasks/task_update.html', {'task': task})