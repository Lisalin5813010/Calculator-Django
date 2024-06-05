from django.db import models

class DiaryItem(models.Model):
    content = models.TextField(max_length=200)

class TodoListItem(models.Model):
    content = models.TextField()


class Student(models.Model):
    student_name = models.TextField(max_length=30,default='')
    student_id = models.IntegerField(default=0)
    student_age = models.IntegerField(default=0)
    student_gender = models.TextField(max_length=30,default='')

