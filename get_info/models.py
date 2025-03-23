from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255,primary_key=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    USER_ROLE=(
        ('admin','Admin'),
        ('user','User')
    )
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True,max_length=40)
    password = models.CharField(max_length=40)
    role = models.CharField(role=USER_ROLE,default='user')


#from first commit 