from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Activity, User

@login_required
def task_list(request):
    if request.user.role == 'admin':
        tasks = Activity.objects.all()
    else:
        tasks = Activity.objects.filter(assigned_to=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def assign_task(request):
    if request.user.role != 'admin':
        return redirect('task_list')
    if request.method == 'POST':
        task_name = request.POST['task_name']
        task_des = request.POST['task_des']
        assigned_to = User.objects.get(id=request.POST['assigned_to'])
        Activity.objects.create(task_name=task_name, task_des=task_des, assigned_to=assigned_to, created_by=request.user.user_name)
        return redirect('task_list')
    users = User.objects.filter(role='user')
    return render(request, 'tasks/assign_task.html', {'users': users})

@login_required
def complete_task(request, task_id):
    task = Activity.objects.get(id=task_id)
    if request.user.user_id == task.assigned_to.user_id:
        task.status = True
        task.save()
    return redirect('task_list')