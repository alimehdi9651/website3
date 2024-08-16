from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class recipe(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, blank = True, null=True)
    recipe_name = models.CharField(max_length = 100)
    recipe_description = models.TextField()
    recipe_img = models.ImageField()

    

class Department(models.Model):
    department = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']


class Student_ID(models.Model):
    student_id = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.student_id


class Subject(models.Model):
    subject_name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.subject_name



class Student(models.Model):
    department = models.ForeignKey(Department, related_name = "depart", on_delete = models.CASCADE)
    student_id = models.OneToOneField(Student_ID, related_name = "stu_id", on_delete = models.CASCADE)
    student_name= models.CharField(max_length = 100)
    student_email = models.EmailField(unique = True)
    student_age = models.IntegerField(default = 18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta():
        ordering = ['student_name']
        verbose_name = "student"

class Subject_mark(models.Model):
    student = models.ForeignKey(Student, related_name = "std_marks", on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    marks = models.IntegerField()
    
    def __str__(self) ->str:
        return f'{self.student.student_name} {self.subject.subject_name}'    
    
    class Meta:
        ordering = ['student']
        unique_together = ['student','subject']

    
class Report_card(models.Model):
    student = models.ForeignKey(Student, related_name="studentreportcard", on_delete = models.CASCADE)
    student_rank = models.IntegerField()
    date_of_generation = models.DateField(auto_now_add = True)
    
    class Meta():
        unique_together = ['student_rank', 'date_of_generation']