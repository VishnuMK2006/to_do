from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('title','created_at','completed')

#At finally modify the admin panel
# admin.site.register(Task,TaskAdmin)

#NOTE: if the model already registered in admin , if you try to register it again it makes error.
"""
Here you modify the admin page for easy visualization.
                                                     |---|->model name(table)
to get the admin page: localhost:3000/admin/get_info/task  # everything should be in small letter.
                                           |--------|->app name
"""