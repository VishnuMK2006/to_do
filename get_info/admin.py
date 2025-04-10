from django.contrib import admin

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('user_id','user_name','role','email')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'status', 'urgency', 'assin_to', 'due_at', 'created_by_user','general_task','gnrl_pickup') 
