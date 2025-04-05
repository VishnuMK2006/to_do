from django.urls import path
from . import views
urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_task, name='add_task'),
    path('remove/', views.remove_task, name='remove_task'),
    path('complete/', views.complete_task, name='complete_task'),
    path('admin_user_list/', views.admin_user_list, name='admin_user_list'),
    path('assign_task/', views.assign_task, name='assign_task'),
    path('user_tasks/<int:user_id>/', views.user_task_detail, name='user_task_detail'),
]
