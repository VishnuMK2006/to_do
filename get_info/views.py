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
        row=Task.objects.get(title=title)#get the Entire row related to this title
        row.completed= True
        row.save()
    return redirect('todo_list')

