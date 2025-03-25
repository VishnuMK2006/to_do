from django.contrib import admin

from .models import *

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('title','created_at','completed')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('user_id','user_name','role')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display=('task_id','task_name','task_des','assin_to','status','created_by')
