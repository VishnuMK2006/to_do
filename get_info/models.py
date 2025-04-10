from django.db import models
from django.utils import timezone

class User(models.Model):
    USER_ROLE = (
        ('admin', 'Admin'),
        ('user', 'User')
    )
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=40)
    password = models.CharField(max_length=40)
    role = models.CharField(choices=USER_ROLE, max_length=40, default='user')
    email = models.EmailField(unique=True)


class Activity(models.Model):
    URGENCY = (
        ('urgent', 'Urgent'),
        ('moderate', 'Moderate'),
        ('doLater', 'DoLater'),
        ('general','General'),
    )
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=40)
    task_des = models.TextField()
    assin_to = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    status = models.BooleanField(default=False)
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tasks")
    urgency = models.CharField(choices=URGENCY, max_length=40, default='moderate')
    files = models.FileField(upload_to='task_files/', null=True, blank=True)
    due_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    general_task = models.BooleanField(default=False)
    gnrl_pickup = models.CharField(max_length=40,blank=True,default="")

    def is_overdue(self):
        return not self.status and self.due_at and timezone.now() > self.due_at

    def was_late(self):
        return self.completed_at and self.due_at and self.completed_at > self.due_at


