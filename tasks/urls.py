from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('assign/', views.assign_task, name='assign_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
]