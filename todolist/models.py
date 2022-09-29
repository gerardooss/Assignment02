from operator import length_hint
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length = 150)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)