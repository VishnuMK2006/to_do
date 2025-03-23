from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255,primary_key=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

