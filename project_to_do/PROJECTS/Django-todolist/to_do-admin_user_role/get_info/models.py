from django.db import models

class User(models.Model):
    USER_ROLE = (
        ('admin', 'Admin'),
        ('user', 'User')
    )
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=40)
    password = models.CharField(max_length=40)
    role = models.CharField(choices=USER_ROLE, max_length=40, default='user')


class Activity(models.Model):
    URGENCY = (
        ('urgent', 'Urgent'),
        ('moderate', 'Moderate'),
        ('doLater', 'DoLater')
    )
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=40)
    task_des = models.CharField(max_length=400)
    assin_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_by=models.CharField(max_length=40)
    urgency = models.CharField(choices=URGENCY, max_length=40, default='moderate')
    files = models.FileField(upload_to='task_files/', null=True, blank=True)
