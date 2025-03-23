from django.urls import path
from . import views
urlpatterns=[
    path('todo/',views.todo_list, name='todo_list'),
    path('add/',views.add_task,name='add_task'),
    path('remove/',views.remove_task,name='remove_task'),
    path('complete/',views.complete_task,name='complete_status'),
]