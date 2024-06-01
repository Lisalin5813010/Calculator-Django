from django.db import models



class DiaryItem(models.Model):
    content = models.TextField(max_length=200)

class TodoListItem(models.Model):
    content = models.TextField()


class Student(models.Model):
    Name = models.TextField(max_length=30)
    Id = models.IntegerField(max_length=30)
    Age = models.IntegerField(max_length=30)
