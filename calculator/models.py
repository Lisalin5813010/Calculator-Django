from django.db import models
from django.contrib.auth.models import AbstractUser



class DiaryItem(models.Model):
    content = models.TextField(max_length=200)

class TodoListItem(models.Model):
    content = models.TextField()

