from django.urls import path
from . import views
urlpatterns=[
    path('admin_task_assignment/<int:user_id>/',views.admin_user_list,name='admin_user_list'),
    path('t_submit/<int:user_id>/',views.assign_task,name='assign_task'),
    path('signup/',views.signup_area,name='signup_area'),
    path('login/',views.login_area,name='login_area'),
    path('task-assign/<int:user_id>/', views.task_assign, name='task_assign'),
    path('task-complete/<int:user_id>/', views.mark_completed, name='mark_completed'),

]