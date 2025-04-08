from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib import messages 
from django.utils import timezone
from datetime import datetime

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')  
        Task.objects.create(title=title)  
    return redirect('todo_list')  

def remove_task(request):
    if request.method == 'POST':
        title = request.POST.get('rmvtitle') 
        Task.objects.filter(title=title).delete()
    return redirect('todo_list')

def complete_task(req):
    if req.method == 'POST':
        title = req.POST.get('cmptitle')
        row=Task.objects.get(title=title)
        row.completed= not row.completed
        row.save()
    return redirect('todo_list')

##admin user list code
def admin_user_list(request,user_id):
    user = get_object_or_404(User, user_id=user_id)
    task_list = Activity.objects.filter(created_by_user=user,general_task=False)
    user_list=User.objects.filter(role='user')
    gnl_list=Activity.objects.filter(general_task=True,created_by_user=user_id)
    return render(request,'get_info/task_assign.html', {'user_list':user_list,'task_list':task_list,'admin': user,'general_list':gnl_list})


### assign task
def assign_task(request, user_id):
    user = get_object_or_404(User, user_id=user_id)

    if request.method == 'POST':
        t_title = request.POST.get('task_name')
        t_des = request.POST.get('task_des')
        t_assign_to = request.POST.get('assin_to')
        urgency = request.POST.get('urgency')
        files = request.FILES.get('files')
        due_date_str = request.POST.get("due_date")

        due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None

        if t_assign_to == "general":
            Activity.objects.create(
                task_name=t_title,
                task_des=t_des,
                general_task=True,
                created_by_user=user,
                urgency=urgency,
                files=files,
                due_at=due_date,
                gnrl_pickup="General"
            )
        else:
            user_instance = get_object_or_404(User, user_id=t_assign_to)
            Activity.objects.create(
                task_name=t_title,
                task_des=t_des,
                assin_to=user_instance,
                created_by_user=user,
                urgency=urgency,
                files=files,
                due_at=due_date
            )

    return redirect('admin_user_list', user_id=user_id)


## sign up details to insert
def signup_area(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(user_name=username).exists():
            messages.error(request, "User with these credentials already exists! Try a different username.")
        else:
            User.objects.create(
                user_name=username,
                password=password,
            )
            messages.success(request,'user Created Successfully')
            return redirect('login_area')
    return render(request,'get_info/signup.html')

##login details checkup
def login_area(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(user_name=username, password=password).first()
        if user:
            messages.success(request, f'Welcome, {username}!')
            current_user= User.objects.get(user_name=username)
            role=current_user.role
            if role == 'admin' or role== 'Admin':
                return redirect('admin_user_list', user_id=user.user_id)
            else:
                return redirect('task_assign', user_id=user.user_id)
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'get_info/login.html')

def task_assign(request, user_id):
    user = get_object_or_404(User, user_id=user_id)
    task_list = Activity.objects.filter(assin_to=user)
    gnl_list=Activity.objects.filter(general_task=True)
    return render(request, 'get_info/user_task.html', {'user': user,'task':task_list,'general_task': gnl_list })### general task assign


### for status button
def mark_completed(request, user_id):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        status_value = request.POST.get('status')
        task = get_object_or_404(Activity, task_id=task_id, assin_to__user_id=user_id)

        if status_value == "complete":
            task.status = True
            task.completed_at = timezone.now()
        else:
            task.status = False
            task.completed_at = None
        task.save()

    return redirect('task_assign', user_id=user_id)

###file upload
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "task_assign.html")


def dashboard_redirect(request):
    if request.user.role == 'admin':
        return redirect('admin_user_list', user_id=request.user.user_id)
    else:
        return redirect('task_assign', user_id=request.user.id)
    

### general task pickup

def pickup_task(request, user_id):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Activity, pk=task_id)
        user = get_object_or_404(User, pk=user_id)

        task.assin_to = user
        task.gnrl_pickup = user.user_name
        task.general_task = False 
        task.save()

        return redirect('task_assign', user_id=user_id)



    
    
    