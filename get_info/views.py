from django.shortcuts import render, redirect
from .models import *

def todo_list(request):
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'get_info/todo.html', {'tasks': tasks}) #{'tasks': tasks},here LHS 'tasks'->act as an list have the all tasks details fetched.

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Get title from form
        Task.objects.create(
            title=title
            )  # Method to INSERT(Alias) record into table.
    return redirect('todo_list')  # Redirect to to-do list after insert records

def remove_task(request):
    if request.method == 'POST':
        title = request.POST.get('rmvtitle') #get the record title via button
        Task.objects.filter(title=title).delete()
    return redirect('todo_list')

def complete_task(req):
    if req.method == 'POST':
        title = req.POST.get('cmptitle')
        try:
            row = Task.objects.get(title=title)
            row.completed = True
            row.save()
        except Task.DoesNotExist:
            pass  # Or handle it gracefully
    return redirect('todo_list')


##admin user list code
def admin_user_list(request):
    task_list=Activity.objects.all()
    user_list=User.objects.filter(role='user')
    return render(request,'get_info/task_assign.html', {'user_list':user_list,'task_list':task_list})

def assign_task(request):
    if request.method == 'POST':
        t_title=request.POST.get('task_name')
        t_des=request.POST.get('task_des')
        t_assign_to = request.POST.get('assin_to')
        t_assign_by = request.POST.get('admin_id')
        user_instance = User.objects.get(user_id=t_assign_to)#get the object first based on the id tassign the obj to the foreginkey variable
        Activity.objects.create(
            task_name=t_title,
            task_des=t_des,
            assin_to=user_instance,
            created_by=t_assign_by,
        )
    return redirect('admin_user_list')

##user - tasks assigned to user
def user_task_detail(request, user_id):
    user = User.objects.get(pk=user_id)
    tasks = Activity.objects.filter(assin_to=user)
    return render(request, 'get_info/user_task_detail.html', {
        'selected_user': user,
        'tasks': tasks
    })
