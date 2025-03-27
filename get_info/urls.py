from django.urls import path
from . import views
urlpatterns=[
    path('admin_task_assignment/',views.admin_user_list,name='admin_user_list'),
    path('t_submit/',views.assign_task,name='assign_task'),
]