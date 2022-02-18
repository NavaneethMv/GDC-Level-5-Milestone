from django.shortcuts import render, redirect
from tasks.models import Task

def index_view(request):
    return redirect("/tasks")

def task_view(request):
    task = Task.objects.all().filter(deleted=False).filter(completed=False)
    search_term = request.GET.get("search")
    if search_term:
        task = task.filter(title__icontains=search_term)
    return render(request, "tasks.html", {"tasks": task})

def add_task_view(request):
    task = request.GET.get("task")
    task_obj = Task(title=task)
    task_obj.save()
    return redirect("/tasks")

def delete_task_view(request, index):
    Task.objects.filter(id=index).update(deleted=True)
    return redirect("/tasks")

def complete_task_view(request, index):
    Task.objects.filter(id=index).update(completed=True)
    return redirect("/tasks")

def completed_tasks_view(request):
    completed_tasks = Task.objects.filter(deleted=False).filter(completed=True)
    return render(request, "completed_tasks.html", {"completed_tasks": completed_tasks})

def all_tasks_view(request):
    all_tasks = Task.objects.filter(deleted=False)
    completed_tasks = all_tasks.filter(completed=True)
    pending_tasks = all_tasks.filter(completed=False)
    return render(request, "all_tasks.html", {"completed_tasks": completed_tasks, "pending_tasks": pending_tasks})