from django.urls import path
from . import views
urlpatterns=[
    path('admin_task_assignment/',views.admin_user_list,name='admin_user_list'),
    path('t_submit/',views.assign_task,name='assign_task'),
    path('signup/',views.signup_area,name='signup_area'),
    path('login/',views.login_area,name='login_area'),
]